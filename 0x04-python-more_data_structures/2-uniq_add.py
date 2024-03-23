#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqlist = set(my_list)
    num = 0

    for i in uniqlist:
        num += i
    return num
