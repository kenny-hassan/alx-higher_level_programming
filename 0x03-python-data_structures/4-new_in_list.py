#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    a = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1:
        return a.copy()
    else:
        a[idx] = element
        return a
