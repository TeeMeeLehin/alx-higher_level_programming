#!/usr/bin/python3

def subpow(a, b):
    ans = a
    while(b > 1):
        ans *= a
        b -= 1
    return ans


def pow(a, b):
    if (b == 0):
        return (1)
    if (b > 0):
        return (subpow(a, b))
    if (b < 0):
        return (1/(subpow(a, -b)))
