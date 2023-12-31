#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    el_printed = 0
    for i in range(0, x):
        try:
            print(f"{my_list[i]}", end='')
            el_printed += 1
        except IndexError:
            break
    print()
    return el_printed
