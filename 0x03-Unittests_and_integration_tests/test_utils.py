#!/usr/bin/env python3
"""Module for testing utils.access_nested_map"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Class for testing access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),  # test simple dictionary access
        ({"a": {"b": 2}}, ("a",), {"b": 2}),  # test nested dictionary access
        ({"a": {"b": 2}}, ("a", "b"), 2)  # test deep nested dictionary access
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test method for access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

