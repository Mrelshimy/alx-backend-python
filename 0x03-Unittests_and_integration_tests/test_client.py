#!/usr/bin/env python3
""" utils.py test module """
import unittest
from unittest.mock import Mock, patch
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
