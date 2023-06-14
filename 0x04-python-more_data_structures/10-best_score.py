#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        scores = list(a_dictionary.values())
        max = scores[0]
        for i in range(len(scores) - 1):
            max = max if max > scores[i + 1] else scores[i + 1]
        for key, value in a_dictionary.items():
            if value == max:
                return key
    else:
        return None