#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = 0
        c = a / b
    except (ZeroDivisionError, TypeError):
        c = None
    finally:
        print("Inside result: {}".format(c))
        return c
