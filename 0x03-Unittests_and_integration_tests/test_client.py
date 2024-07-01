#!/usr/bin/env python3
""" utils.py test module """
import unittest
from unittest.mock import Mock, patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ client.py GithubOrgClient test class """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, url, mock_get):
        """ GithubOrgClient test method """
        mock_responce = {'a': 'b'}
        mock_get.return_value = mock_responce
        obj = GithubOrgClient(url)
        result = obj.org
        self.assertEqual(result, mock_responce)
        mock_get.called_with_once(obj.ORG_URL)

    def test_public_repos_url(self):
        """ test_public_repos_url method """
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as org_mock:
            org_mock.return_value = 'abc'
            obj = GithubOrgClient('abc')
            self.assertEqual(obj._public_repos_url, 'abc')

    @patch('client.get_json')
    def test_public_repos(self, mock_get):
        """ test_public repos method """
        return_value = {'a': 'b'}
        mock_get.return_value = return_value
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as org_mock:
            org_mock.return_value = 'abc'

    @parameterized.expand([
        ({'license': {"key": "my_license"}}, "my_license", True),
        ({'license': {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """ test has_license method """
        obj = GithubOrgClient('abc')
        result = obj.has_license(repo, license_key)
        self.assertEqual(result, expected)
