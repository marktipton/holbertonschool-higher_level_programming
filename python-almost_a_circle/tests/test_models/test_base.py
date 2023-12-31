#!/usr/bin/python3
"""unittest for base"""
import unittest
import json
from models.base import Base


class TestBase(unittest.TestCase):
    """test base class"""
    def test_invalid_id(self):
        invalid_id = -1
        with self.assertRaises(ValueError):
            instance = Base(invalid_id)

    def test_id_input(self):
        obj1 = Base(23)
        self.assertEqual(obj1.id, 23)

    def test_float_id(self):
        obj = Base(2.718)
        self.assertEqual(2.718, obj.id)

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class Test_to_json_string(unittest.TestCase):
    """test for to_json_string method"""
    def test_empty(self):
        self.assertEqual(Base.to_json_string([]), '[]')

    def test_none(self):
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_dictionary(self):
        test_dict = {'width': 1, 'height': 3, 'x': 5, 'y':7, 'id': 9}
        self.assertTrue(type(Base.to_json_string(test_dict) is str))

class Test_save_to_file(unittest.TestCase):
    """test for to_json_string method"""
    pass


class Test_from_json_string(unittest.TestCase):
    """test for to_json_string method"""
    def test_empty(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string([]), [])


class Test_Create(unittest.TestCase):
    """test for to_json_string method"""
    pass


class Test_load_from_file(unittest.TestCase):
    """test for to_json_string method"""
    pass

if __name__ == "__main__":
    unittest.main()