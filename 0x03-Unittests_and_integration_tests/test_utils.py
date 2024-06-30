#!/usr/bin/env python3
""" utils.py test module """
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ utils.py test class """

    @parameterized.expand([
        ({"a": {"b": {"c": 1}}}, "abc", 1),
        ({"a": {"b": {"c": 1}}}, "a", {"b": {"c": 1}}),
        ({"a": {"b": {"c": 1}}}, [], {"a": {"b": {"c": 1}}}),
    ])
    def test_access_nested_map(self, input, path, expected):
        """ test_access_nested_map test method """
        self.assertEqual(access_nested_map(input, path), expected)
