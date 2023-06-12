#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    ans = my_list[0]
    for i in range(len(my_list) - 1):
        ans = ans if ans > my_list[i + 1] else my_list[i + 1]
    return ans
