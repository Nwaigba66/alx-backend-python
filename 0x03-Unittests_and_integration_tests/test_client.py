#!/usr/bin/env python3
"""This module tests classes in the client module
"""

from unittest import TestCase
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(TestCase):
    """Define tests for org
    """
    @parameterized.expand([
        ("google",), ("abc",)])
    @patch('client.get_json')
    def test_org(self, url, org_get_json):
        """test the org method
        """
        my_class = GithubOrgClient(url)
        result = my_class.org()
        org_get_json.assert_called_once_with(my_class.ORG_URL.format(org=url))

    def test_public_repos_url(self):
        """test the public-repos_url property
        """
        test_url = "https://abc_test_repo.com"
        test_org = "abc"
        value = {"repos_url": test_url}
        with patch.object(
                GithubOrgClient, 'org',
                new_callable=PropertyMock) as mock_object:
            mock_object.return_value = value
            my_class = GithubOrgClient(test_org)
            result = my_class._public_repos_url
            self.assertEqual(result, test_url)
