#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test case for the max_integer_function

    """

    def test_typeErrors(self):
        self.assertRaises(TypeError, max_integer, 4)
        self.assertRaises(TypeError, max_integer, 0.5)
        self.assertRaises(TypeError, max_integer, -2)
        self.assertRaises(TypeError, max_integer, 6j)
        self.assertRaises(TypeError, max_integer, [2j, 0])
        self.assertRaises(TypeError, max_integer, [12, "90"])

    def test_normalResults(self):
        self.assertEqual(max_integer([2, 4, 3]), 4)
        self.assertEqual(max_integer([-1000000, 10, 12, -13]), 12)
