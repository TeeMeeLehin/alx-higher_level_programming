#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    sum = 0
    for x in my_list:
        if x in new_list:
            pass
        else:
            new_list.append(x)
            sum += x
    return sum
