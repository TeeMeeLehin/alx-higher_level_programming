#!/usr/bin/python3
def element_at(my_list, idx):
    n = len(my_list)
    if (idx < 0):
        return None
    if (idx > (n - 1)):
        return None
    num = my_list[idx]
    return num
