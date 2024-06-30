#!/usr/bin/env python3
""" utils.py test module """
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """ utils.py access_nested_map test class """

    @parameterized.expand([
        ({"a": {"b": {"c": 1}}}, "abc", 1),
        ({"a": {"b": {"c": 1}}}, "a", {"b": {"c": 1}}),
        ({"a": {"b": {"c": 1}}}, [], {"a": {"b": {"c": 1}}}),
    ])
    def test_access_nested_map(self, input, path, expected):
        """ test_access_nested_map test method """
        self.assertEqual(access_nested_map(input, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, input, path, expected):
        """ test_access_nested_map_exception test method """
        with self.assertRaises(expected):
            access_nested_map(input, path)


class TestGetJson(unittest.TestCase):
    """ utils.py get_json test class """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, expected, mock_get):
        """ test get json method """

        mock_get.return_value.json.return_value = expected
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, expected)
