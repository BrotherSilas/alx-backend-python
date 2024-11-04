#!/usr/bin/env python3
"""
Unit tests for utils.access_nested_map function.
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Dict, Tuple, Union


class TestAccessNestedMap(unittest.TestCase):
    """
    Test class for testing access_nested_map function.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int]
            ) -> None:
        """
        Test access_nested_map function returns expected results.
        
        Args:
            nested_map: A dictionary that may contain nested dictionaries
            path: A tuple of strings representing the path to access
            expected: Expected result from the function
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: str
            ) -> None:
        """
        Test access_nested_map function raises KeyError with expected messages.
        
        Args:
            nested_map: A dictionary that may contain nested dictionaries
            path: A tuple of strings representing the path to access
            expected: Expected key in the KeyError message
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{expected}'")


if __name__ == '__main__':
    unittest.main()

