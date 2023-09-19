#!/usr/bin/python3
"""unittest for max_integer"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test(self):
        self.assertTrue(max_integer)

    def test_negative(self):
        self.assertEqual(max_integer([-3, -7, -9]), -3)

    def test_middle_max(self):
        self.assertEqual(max_integer([4, 30, 15]), 30)

    def test_end_max(self):
        test_max = max_integer([15, 20, 25])
        self.assertEqual(test_max, 25, "should return max if el at end")

    def test_one_element(self):
        self.assertEqual(max_integer([5]), 5)

    def list_empty(self):
        self.assertEqual(max_integer([]), 1)
