#!/usr/bin/env python3
"""This module define test for the assess_nested_map of thr utils module
"""
from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestMemoize(TestCase):
    """Define tests for memoize function
    """

    def test_memoize(self):
        """test the memoize function
        """

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_memo:
            my_class = TestClass()
            my_class.a_property  # first call
            my_class.a_property  # second call
            mock_memo.assert_called_once()


class TestAccessNestedMap(TestCase):
    """Define Tests for access_nested_map
    """

    @parameterized.expand([
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, nested, path, output):
        """Test that function works as expected"""
        self.assertEqual(access_nested_map(nested, path), output)

    @parameterized.expand([
            ({}, ("a",), "a"),
            ({"a": 1}, ("a", "b"), "b")])
    def test_access_nested_map_exception(self, nested, path, error_msg):
        """Test that KeyError is thrown"""
        with self.assertRaisesRegex(KeyError, error_msg):
            access_nested_map(nested, path)


class TestGetJson(TestCase):
    """Define tests for the get_json function in the utils module
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})])
    @patch('utils.requests.get')
    def test_get_json(self, url, response, mock_get):
        """Implement test for the get_json function
        """
        mock_get.return_value.json.return_value = response
        result = get_json(url)
        self.assertEqual(result, response)
