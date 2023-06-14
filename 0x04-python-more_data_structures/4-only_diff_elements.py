#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    agg = set.union(set_1, set_2)
    union = set.intersection(set_1, set_2)
    exclusive = {x for x in agg if x not in union}
    return exclusive
