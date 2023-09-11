#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string == None or type(roman_string) != str:
        return 0
    count = 0
    for c in roman_string:
        if c == 'I':
            count += 1
        elif c == 'V':
            count += 5
        elif c == 'X':
            count += 10
        elif c == 'L':
            count += 50
        elif c == 'C':
            count += 100
        elif c == 'D':
            count += 500
        elif c == 'M':
            count += 1000
    return count
        

