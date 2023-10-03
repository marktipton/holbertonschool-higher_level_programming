#!/usr/bin/python3
"""unittest for base"""
import unittest
from unittest.mock import patch
import io
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

    def test_width_nonint(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.s.size = "s"
            Square("s", 1, 1, 45)

    def test_height_nonint(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.s.size = [2, 3]
            Square([2, 3], 1, 1, 45)

    def test_x_nonint(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.s.x = {2, 20}
            Square(2, {2, 20}, 1, 45)

    def test_y_nonint(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.s.y = (8, 12)
            Square(2, 1, (8, 12), 45)

    def test_width_neg(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.s.size = -1
            Square(-1, 1, 1, 45)

    def test_height_neg(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.s.size = -4
            Square(-4, 1, 1, 45)

    def test_x_neg(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            self.s.x = -345
            Square(2, -345, 1, 45)

    def test_y_neg(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            self.s.y = -60
            Square(2, 1, -60, 45)

    def test_width_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.s.size = 0
            Square(0, 1, 1, 45)

    def test_height_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.s.size = 0
            Square(0, 1, 1, 45)


class Test_update(unittest.TestCase):
    """test update method for square"""
    pass


class Test_to_dictionary(unittest.TestCase):
    """test to_dictionary method for square"""
    pass

class Test_display(unittest.TestCase):
    """test diplay method"""
    def setUp(self):
        self.s = Square(2, 0, 0, 50)

    def test_display(self):
        with patch("sys.stdout", new=io.StringIO()) as check:
            self.s.display()
            self.assertEqual(check.getvalue(), "##\n##\n")
