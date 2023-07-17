#!/usr/bin/python3
"""test scipt for rectangle class"""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    test class for rectangle class
    """
    def test_rectangle_init(self):
        "testing class initialization"
        rect = Rectangle(4, 5, 2, 3, 8)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.id, 8)

    def test_width_getter(self):
        "testing the property getter for width"
        rect = Rectangle(2, 4)
        self.assertEqual(rect.width, 2)

    def test_height_getter(self):
        "testing the property getter for heigth"
        rect = Rectangle(2, 4)
        self.assertEqual(rect.height, 4)

    def test_x_getter(self):
        "testing the property getter for x"
        rect = Rectangle(2, 4)
        self.assertEqual(rect.x, 0)

    def test_y_getter(self):
        "testing the property getter for y"
        rect = Rectangle(2, 4, 0, 3)
        self.assertEqual(rect.y, 3)

    def test_weight_validation(self):
        "testing the validation of weight attr"
        with self.assertRaises(TypeError):
            rect = Rectangle("2", 5)
        with self.assertRaises(ValueError):
            rect2 = Rectangle(-2, 5)
    
    def test_height_validation(self):
        "testing the validation of height attr"
        with self.assertRaises(TypeError):
            rect = Rectangle(5, "0")
        with self.assertRaises(ValueError):
            rect2 = Rectangle(2, -5)

    def test_x_validation(self):
        "testing the validation of x attr"
        with self.assertRaises(TypeError):
            rect = Rectangle(2, 5, "x")
        with self.assertRaises(ValueError):
            rect2 = Rectangle(2, 5, -1)

    def test_y_validation(self):
        "testing the validation of y attr"
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 5, 3, "y")
        with self.assertRaises(ValueError):
            rect2 = Rectangle(2, 3, 4, -9)
    
    def test_area(self):
        "testing the area method"
        rect = Rectangle(3, 4, 2, 1, 34)
        self.assertEqual(rect.area(), 12)
    
    @staticmethod
    def capture_stdout(rect, method):
        "Captures and returns text printed to stdout"
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture
    
    def test_display(self):
        "testing the display method"
        rect = Rectangle(2, 3)
        expected_output = "##\n##\n##\n"
        capture = self.capture_stdout(rect, "display")
        self.assertEqual(expected_output, capture.getvalue())


    def test_str(self):
        "testing the str method"
        rect = Rectangle(1, 2, 3, 4, 5)
        expected_output = "[Rectangle] (5) 3/4 - 1/2"
        result = str(rect)
        self.assertEqual(result, expected_output)

    def test_update(self):
        "testing the update method"
        rect = Rectangle(2, 3)
        rect.update(23, 3, 6, 9, 12)
        self.assertEqual(rect.id, 23)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 6)
        self.assertEqual(rect.x, 9)
        self.assertEqual(rect.y, 12)
        rect2 = Rectangle(2, 3)
        rect2.update(y=3, width=7, height=4)
        self.assertEqual(rect2.width, 7)
        self.assertEqual(rect2.height, 4)
        self.assertEqual(rect2.y, 3)

    def test_to_dictionary(self):
        "testing the to_dictionary method"
        rect = Rectangle(2, 3, 4, 5, 6)
        expected_dict = {"width" : 2, "height" : 3, "x" : 4, "y" : 5, "id" : 6}
        res = rect.to_dictionary()
        self.assertEqual(expected_dict, res)

if __name__ == '__main__':
    unittest.main()
