#!/usr/bin/python3
"""unittest for base"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """test rectangle class"""
    def setUp(self):
        self.r = Rectangle(2, 3, 1, 1, 45)

    def test_width_getter(self):
        self.assertEqual(self.r.width, 2)

    def test_height_getter(self):
        self.assertEqual(self.r.height, 3)

    def test_x_getter(self):
        self.assertEqual(self.r.x, 1)

    def test_y_getter(self):
        self.assertEqual(self.r.y, 1)

    def test_width_setter(self):
        self.r.width = 4
        self.assertEqual(self.r.width, 4)

    def test_height_setter(self):
        self.r.height = 1
        self.assertEqual(self.r.height, 1)

    def test_x_setter(self):
        self.r.x = 2
        self.assertEqual(self.r.x, 2)

    def test_y_setter(self):
        self.r.y = 3
        self.assertEqual(self.r.y, 3)


class Test_area(unittest.TestCase):
    """test area method"""
    pass


class Test_display(unittest.TestCase):
    """test diplay method"""
    pass


class Test_update(unittest.TestCase):
    """test update method"""
    pass


class Test_to_dictionary(unittest.TestCase):
    """test to_dictionary method"""
    pass
