#!/usr/bin/python3
"""Instance of a square class"""


class Square():
    """Instance of a square class"""

    def __init__(self, num=0, pos=(0, 0)):
        self.__size = num
        self.__position = pos
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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if not isinstance(value, tuple) and not len(value) == 2 and \
           not all(isinstance(i, int) for i in value):
            raise TypeError("position must be a tuple of 2 positive")

    def area(self):
        return self.__size**2

    def my_print(self):
        num = self.size
        pos = self.position
        if num == 0:
            print("")
        for i in range(pos[1]):
            [print("")]
        for i in range(num):
            [print(" ", end="") for j in range(pos[0])]
            [print("#", end="") for k in range(num)]
            print("")
