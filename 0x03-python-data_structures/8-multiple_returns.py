#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    f = sentence[0] if length > 0 else None
    res = (length, f)
    return res
