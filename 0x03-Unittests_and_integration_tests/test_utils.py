#!/usr/bin/env python3
"""TestAccessNestedMap module
"""



import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Test cases for the `access_nested_map` function from the `utils` module.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Tests the `access_nested_map` function
        to ensure it returns the correct values.
        
        Parameters:
        - nested_map: The dictionary to traverse.
        - path: The tuple representing the path of keys to access.
        - expected: The expected result after traversing the dictionary.

        Asserts that the `access_nested_map` function
        returns the expected value for given inputs.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
