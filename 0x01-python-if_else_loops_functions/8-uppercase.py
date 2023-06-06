#!/usr/bin/python3

def uppercase(str):
    for char in str:
        num = ord(char)
        if num in range(97, 123):
            char = chr(num - 32)
        print("{}".format(char), end="")
    print("")
