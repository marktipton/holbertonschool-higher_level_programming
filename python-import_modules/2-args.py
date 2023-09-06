#!/usr/bin/python3

from sys import argv
if __name__ == "__main__":
    n_args = len(argv) - 1
    print(f"{n_args}", end=" ")
    if n_args == 1:
        print("argument:")
    elif n_args == 0:
        print("arguments.")
    else:
        print("arguments:")
    for n in range(1, n_args + 1):
        print("{:d}: {}".format(n, argv[n]))
