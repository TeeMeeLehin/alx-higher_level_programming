#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    sum = 0
    weights = 0
    for pair in my_list:
        sum += (pair[0] * pair[1])
        weights += pair[1]
    return (sum / weights)
