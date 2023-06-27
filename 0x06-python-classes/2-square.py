#!/usr/bin/python3
"""Instance of a square class"""


class Square():
    """Instance of a square class"""

    def __init__(self, num=0):
        self.__size = num
        if not isinstance(num, int):
            raise TypeError("size must be an integer")
        elif (num < 0):
            raise ValueError("size must be >= 0")
