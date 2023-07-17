#!/usr/bin/python3
"""test scipt for base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


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
    
    def test_to_json(self):
        "testing the to_json method"
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")
        data = [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]
        result = Base.to_json_string(data)
        self.assertEqual(result, '[{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]')

    def test_save_to_file(self):
        "testing the save_to_file function"
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            content = file.read()
        self.assertEqual(content, "[]")
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            content = file.read()
        self.assertEqual(content, "[]")
        class_instance_1 = Rectangle(2, 3)
        class_instance_2 = Rectangle(3, 4)
        class_instance_1.update(id=3)
        class_instance_2.update(id=4)
        Rectangle.save_to_file([class_instance_1, class_instance_2])
        with open("Rectangle.json", "r") as file:
            content = file.read()
        expected = '[{"id": 3, "width": 2, "height": 3, "x": 0, "y": 0}, {"id": 4, "width": 3, "height": 4, "x": 0, "y": 0}]'
        self.assertEqual(content, expected)
        pass

if __name__ == '__main__':
    unittest.main()
