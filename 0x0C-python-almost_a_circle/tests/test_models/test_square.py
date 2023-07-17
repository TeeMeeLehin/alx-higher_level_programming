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
    
    def test_update(self):
        "testing the update method"
        rect = Square(2)
        rect.update(23, 3, 9, 12)
        self.assertEqual(rect.id, 23)
        self.assertEqual(rect.size, 3)
        self.assertEqual(rect.x, 9)
        self.assertEqual(rect.y, 12)
        rect2 = Square(3)
        rect2.update(y=3, size=4)
        self.assertEqual(rect2.size, 4)
        self.assertEqual(rect2.y, 3)
    
    def test_to_dictionary(self):
        pass

if __name__ == '__main__':
    unittest.main()
    


