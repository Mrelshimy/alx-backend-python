#!/usr/bin/env python3
""" utils.py test module """
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


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
    def test_get_json(self, test_url, expected, get_mock):
        """ test get json method """
        get_mock.return_value.json.return_value = expected
        result = get_json(test_url)
        get_mock.assert_called_once_with(test_url)
        self.assertEqual(result, expected)


class TestMemoize(unittest.TestCase):
    """ Test Memoize class """
    def test_memoize(self):
        """ test memoize method """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method', return_value=42) as a_mock:
            new_obj = TestClass()
            new_obj.a_property
            new_obj.a_property
            a_mock.assert_called_once()
        
