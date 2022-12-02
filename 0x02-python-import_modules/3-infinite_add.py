#!/usr/bin/python3

if __name__ == "__main__":
    "prints the result of the addition of all arguments"
    import sys

    count = len(sys.argv) - 1
    a = 0
    b = 0
    for i in range(count):
        a = int(sys.argv[i + 1])
        b = b + a
    print("{}".format(b))
