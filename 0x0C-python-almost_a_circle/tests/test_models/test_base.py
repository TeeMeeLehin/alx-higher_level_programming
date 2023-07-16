#!/usr/bin/python3
"""test scipt for base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test class for Base class
    """
    def test_base_initialization(self):
        "Testing the initialization of Base with no id provided"
        base = Base()
        self.assertEqual(base.id, 1)

        base2 = Base()
        self.assertEqual(base2.id, 2)

    def test_base_initialization_with_id(self):
        "Testing the initialization of Base with id provided"
        base = Base(100)
        self.assertEqual(base.id, 100)

        base2 = Base(200)
        self.assertEqual(base2.id, 200)


if __name__ == '__main__':
    unittest.main()
