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

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        Test GithubOrgClient._public_repos_url returns the correct URL.
        """
        test_payload = {
                "repos_url": "https://api.github.com/orgs/test_org/repos"
                }
        mock_org.return_value = test_payload

        client = GithubOrgClient("test_org")
        public_repos_url = client._public_repos_url

        self.assertEqual(public_repos_url, test_payload["repos_url"])


if __name__ == "__main__":
    unittest.main()
