#!/usr/bin/python3
"""unittest for base"""
import unittest
from models.square import Square


class TestRectangle(unittest.TestCase):
    """test rectangle class"""
    def setUp(self):
        self.s = Square(2, 1, 1, 45)

    def test_size_getter(self):
        self.assertEqual(self.s.size, 2)

    def test_x_getter(self):
        self.assertEqual(self.s.x, 1)

    def test_y_getter(self):
        self.assertEqual(self.s.y, 1)

    def test_size_setter(self):
        self.s.size = 4
        self.assertEqual(self.s.size, 4)

    def test_x_setter(self):
        self.s.x = 2
        self.assertEqual(self.s.x, 2)

    def test_y_setter(self):
        self.s.y = 3
        self.assertEqual(self.s.y, 3)

class Test_update(unittest.TestCase):
    """test update method for square"""
    pass

class Test_to_dictionary(unittest.TestCase):
    """test to_dictionary method for square"""
    pass
