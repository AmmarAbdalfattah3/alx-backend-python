#!/usr/bin/env python3
"""Test Module
"""


import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


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

    @patch('client.get_json')
    @patch(
        'client.GithubOrgClient._public_repos_url',
        new_callable=PropertyMock
    )
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """
        Test GithubOrgClient.public_repos returns the correct list of repos.
        """
        test_url = "https://api.github.com/orgs/test_org/repos"
        test_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        expected_repos = ["repo1", "repo2", "repo3"]

        mock_public_repos_url.return_value = test_url
        mock_get_json.return_value = test_payload

        client = GithubOrgClient("test_org")
        repos = client.public_repos()

        self.assertEqual(repos, expected_repos)
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with(test_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({"license": None}, "my_license", False),
        ({}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """
        Test GithubOrgClient.has_license returns the correct boolean value.
        """
        client = GithubOrgClient("test_org")
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected_result)

        @classmethod
    def setUpClass(cls):
        """Set up the class by patching requests.get."""
        cls.get_patcher = patch(
            'requests.get', side_effect=cls.mocked_requests_get
        )
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down the class by stopping the patcher."""
        cls.get_patcher.stop()

    @staticmethod
    def mocked_requests_get(url):
        """
        Mocked requests.get to return
        predefined responses based on the URL.
        """
        mock_response = Mock()
        if 'orgs' in url:
            mock_response.json.return_value = org_payload
        elif 'repos' in url:
            mock_response.json.return_value = repos_payload
        return mock_response

    def test_public_repos(self):
        """
        Test that GithubOrgClient.public_repos
        returns the expected repos.
        """
        client = GithubOrgClient('google')
        with patch.object(
            client,
            '_public_repos_url',
            return_value='fake_url'
        ):
            self.assertEqual(client.public_repos(), expected_repos)

    def test_public_repos_with_license(self):
        """
        Test that GithubOrgClient.public_repos with
        a license filter returns the correct repos.
        """
        client = GithubOrgClient('google')
        with patch.object(
            client,
            '_public_repos_url',
            return_value='fake_url'
        ):
            self.assertEqual(
                client.public_repos(license="apache-2.0"), apache2_repos
            )


@parameterized_class([
    {"org_payload": org_payload,
     "repos_payload": repos_payload,
     "expected_repos": expected_repos,
     "apache2_repos": apache2_repos}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test for GithubOrgClient.public_repos method.

    This test class mocks external requests and
    tests the public_repos method.
    """

    @classmethod
    def setUpClass(cls):
        """Set up for the class, mocking requests.get
           with specific payloads.
        """
        cls.get_patcher = patch(
            'requests.get', side_effect=cls.mocked_requests_get
        )
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down the class by stopping the patcher."""
        cls.get_patcher.stop()

    @staticmethod
    def mocked_requests_get(url):
        """
        Mocked requests.get function to return
        specific payloads based on the URL.
        """
        mock_response = Mock()
        if 'orgs' in url:
            mock_response.json.return_value =
            TestIntegrationGithubOrgClient.org_payload
        elif 'repos' in url:
            mock_response.json.return_value =
            TestIntegrationGithubOrgClient.repos_payload
        return mock_response

    def test_public_repos(self):
        """
        Test GithubOrgClient.public_repos to
        ensure it returns the expected repos.
        """
        client = GithubOrgClient('google')
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Test GithubOrgClient.public_repos with a license filter.
        """
        client = GithubOrgClient('google')
        self.assertEqual(
            client.public_repos(license="apache-2.0"), self.apache2_repos
        )


if __name__ == "__main__":
    unittest.main()
