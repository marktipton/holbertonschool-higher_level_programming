#!/usr/bin/python3
"""unittest for base"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test(self):
        self.assertTrue(Rectangle)
