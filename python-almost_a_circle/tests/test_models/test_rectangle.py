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

    def test_width_nonint(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.r.width = "s"

    def test_height_nonint(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.r.height = [2, 3]

    def test_x_nonint(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.r.x = {2, 20}

    def test_y_nonint(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.r.y = (8, 12)

    def test_width_neg(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.r.width = -1

    def test_height_neg(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            self.r.height = -4

    def test_x_neg(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            self.r.x = -345

    def test_y_neg(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            self.r.y = -60

    def test_width_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.r.width = 0

    def test_height_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            self.r.height = 0

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
