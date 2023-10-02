#!/usr/bin/python3
"""unittest for base"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_invalid_id(self):
        invalid_id = -1
        with self.assertRaises(ValueError):
            instance = Base(invalid_id)
