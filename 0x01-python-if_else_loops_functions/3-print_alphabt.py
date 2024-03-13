#!/usr/bin/python3
for z in range(97, 123):
    if z == 113 or z == 101:
        continue
    else:
        print("{}".format(chr(z)), end="")
