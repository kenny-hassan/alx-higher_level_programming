#!/usr/bin/python3
for k in range(100):
    if k == 99:
        print(k)
    else:
        print("{}".format('0' + str(k) if k < 10 else k), end=", ")
