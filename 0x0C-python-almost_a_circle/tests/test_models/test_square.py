#!/usr/bin/python3
"""test scipt for square class"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    test class for square class
    """

    def test_init(self):
        "testing intitalization"
        sq = Square(3, 1, 2, 1)
        self.assertEqual(sq.height, 3)
        self.assertEqual(sq.width, 3)
        self.assertEqual(sq.x, 1)
        self.assertEqual(sq.y, 2)
        self.assertEqual(sq.id, 1)
    
    def test_str(self):
        pass

    def test_size(self):
        "testing the getter and setter of size attr"
        sq = Square(4)
        self.assertEqual(sq.size, 4)
        sq.size = 5
        self.assertEqual(sq.size, 5)
    


