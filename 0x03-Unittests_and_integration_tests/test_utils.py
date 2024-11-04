#!/usr/bin/env python3
"""Unit test for utils.access_nested_map - exception testing"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test class for access_nested_map function"""

    @parameterized.expand([
        ({}, ("a",), "a"),  # empty map
        ({"a": 1}, ("a", "b"), "b")  # missing key
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test that accessing invalid paths raises KeyError"""
        with self.assertRaisesRegex(KeyError, expected):
            access_nested_map(nested_map, path)

