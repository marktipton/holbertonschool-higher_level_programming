#!/usr/bin/python3
"""unittest for base"""
import unittest
from unittest.mock import patch
import io
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
            Rectangle("s", 3, 1, 1, 45)

    def test_height_nonint(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.r.height = [2, 3]
            Rectangle(2, [2, 3], 1, 1, 45)

    def test_x_nonint(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.r.x = {2, 20}
            Rectangle(2, 3, {2, 20}, 1, 45)

    def test_y_nonint(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.r.y = (8, 12)
            Rectangle(2, 3, 1, (8, 12), 45)

    def test_width_neg(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.r.width = -1
            Rectangle(-1, 3, 1, 1, 45)

    def test_height_neg(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            self.r.height = -4
            Rectangle(2, -4, 1, 1, 45)

    def test_x_neg(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            self.r.x = -345
            Rectangle(2, 3, -345, 1, 45)

    def test_y_neg(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            self.r.y = -60
            Rectangle(2, 3, 1, -60, 45)

    def test_width_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.r.width = 0
            Rectangle(0, 3, 1, 1, 45)

    def test_height_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            self.r.height = 0
            Rectangle(2, 0, 1, 1, 45)


class Test_area(unittest.TestCase):
    """test area method"""
    def setUp(self):
        self.r = Rectangle(2, 3, 1, 1, 45)

    def test_area(self):
        self.assertEqual(Rectangle(2, 3).area(), 6)


class Test_display(unittest.TestCase):
    """test diplay method"""
    def setUp(self):
        self.r = Rectangle(2, 2, 0, 0, 50)

    def test_display(self):
        with patch("sys.stdout", new=io.StringIO()) as check:
            self.r.display()
            self.assertEqual(check.getvalue(), "##\n##\n")


class Test_update(unittest.TestCase):
    """test update method"""
    def setUp(self):
        self.r = Rectangle(2, 3, 1, 1, 45)
        self.r.update(1)
        self.assertEqual(self.r.id, 1)
        self.r.update(1, 3)
        self.assertEqual(self.r.width, 3)
        self.r.update(1, 3, 5)
        self.assertEqual(self.r.height, 5)
        self.r.update(1, 3, 5, 7)
        self.assertEqual(self.r.x, 7)
        self.r.update(1, 3, 5, 7, 9)
        self.assertEqual(self.r.y, 9)


class Test_to_dictionary(unittest.TestCase):
    """test to_dictionary method"""
    def setUp(self):
        self.r = Rectangle(2, 3, 1, 1, 45)
