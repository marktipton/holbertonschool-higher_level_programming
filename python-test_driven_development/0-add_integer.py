#!/usr/bin/python3
"""
adds two integers and returns sum
"""

def add_integer(a, b=98):
    """adds integers a and b"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an intger")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return a + b
