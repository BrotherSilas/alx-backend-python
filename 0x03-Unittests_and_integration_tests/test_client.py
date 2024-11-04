#!/usr/bin/env python3
"""Unit tests for client module"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient class"""

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get):
        """Test GithubOrgClient.org returns correct value"""
        test_client = GithubOrgClient(org_name)
        test_client.org()
        mock_get.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """Test _public_repos_url property"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/orgs/google/repos"
            }
            test_client = GithubOrgClient("google")
            self.assertEqual(
                test_client._public_repos_url,
                "https://api.github.com/orgs/google/repos"
            )

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test public_repos method"""
        test_payload = {
            'repos_url': "https://api.github.com/orgs/google/repos",
            'repos': [{"name": "repo1"}, {"name": "repo2"}]
        }
        mock_get_json.return_value = test_payload['repos']

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_pub_repos_url:
            mock_pub_repos_url.return_value = test_payload['repos_url']
            test_client = GithubOrgClient("google")
            self.assertEqual(
                test_client.public_repos(),
                ['repo1', 'repo2']
            )
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test has_license method"""
        test_client = GithubOrgClient("google")
        self.assertEqual(test_client.has_license(repo, license_key), expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Set up class for integration testing"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            """Side effect function for mock"""
            mock_response = Mock()
            if url.endswith("/orgs/google"):
                mock_response.json.return_value = cls.org_payload
            elif url.endswith("/repos"):
                mock_response.json.return_value = cls.repos_payload
            return mock_response

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Tear down class after integration testing"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Integration test for public_repos method"""
        test_client = GithubOrgClient("google")
        self.assertEqual(test_client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Integration test for public_repos with license"""
        test_client = GithubOrgClient("google")
        self.assertEqual(
            test_client.public_repos(license="apache-2.0"),
            self.apache2_repos
        )
