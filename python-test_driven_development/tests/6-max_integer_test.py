#!/usr/bin/python3
"""unittest for max_integer"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test(self):
        self.assertTrue(max_integer)

    def test_negative(self):
        self.assertEqual(max_integer([-3, -7, -9]), -3)
