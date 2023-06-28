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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, num):
        self.__size = num
        if not isinstance(num, int):
            raise TypeError("size must be an integer")
        elif (num < 0):
            raise ValueError("size must be >= 0")
        return num

    def area(self):
        return self.__size**2

    def my_print(self):
        num = self.size
        for i in range(num):
            print("{}".format(num * '#'))
        if num == 0:
            print("")
