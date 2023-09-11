#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a1 = 0
    b1 = 0
    a2 = 0
    b2 = 0
    if tuple_a[0]:
        a1 = tuple_a[0]
    if tuple_a[1]:
        a2 = tuple_a[1]
    if tuple_b[0]:
        b1 = tuple_b[0]
    if tuple_b[1]:
        b2 = tuple_b[1]

    sum1 = a1 + b1
    sum2 = a2 + b2

    return (sum1, sum2)
