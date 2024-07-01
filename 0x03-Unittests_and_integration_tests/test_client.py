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
    def test_public_repos(self, url, mock_get):
        """ test_public repos method """
        return_value = {'a': 'b'}
        mock_get.return_value = return_value
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as org_mock:
            org_mock.return_value = 'abc'
            