#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    total = 0
    n_args = len(argv)
    for n in range(1, n_args):
        total += int(argv[n])

    print(f"{total}")
