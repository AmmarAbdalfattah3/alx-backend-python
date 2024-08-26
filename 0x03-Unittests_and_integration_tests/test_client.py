#!/usr/bin/env python3
"""Test Module
"""


import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test case for GithubOrgClient.org method.
    """

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test GithubOrgClient.org returns correct value.
        """
        expected_json = {"login": org_name}
        mock_get_json.return_value = expected_json

        client = GithubOrgClient(org_name)
        org_data = client.org

        mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}"
                )
        self.assertEqual(org_data, expected_json)


if __name__ == "__main__":
    unittest.main()
