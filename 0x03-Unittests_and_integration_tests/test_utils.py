#!/usr/bin/env python3
"""TestAccessNestedMap module
"""


import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


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
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access_nested_map raises KeyError for invalid paths."""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), f"'{path[-1]}'")


class TestGetJson(unittest.TestCase):
    """Test cases for the get_json function in the utils module."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Test get_json returns the expected result."""
        with patch('utils.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            result = get_json(test_url)

            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Test case for the memoize decorator."""
    def test_memoize(self):
        """Test memoize decorator to ensure method is called only once."""
        class TestClass:
            """Class to demonstrate memoization."""
            def a_method(self):
                """Simple method that returns 42."""
                return 42

            @memoize
            def a_property(self):
                """Simple method that returns 42."""
                return self.a_method()

        with patch.object(
                TestClass, 'a_method', return_value=42
                ) as mock_method:
            test_obj = TestClass()

            self.assertEqual(test_obj.a_property, 42)
            mock_method.assert_called_once()

            self.assertEqual(test_obj.a_property, 42)
            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
