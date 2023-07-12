#!/usr/bin/python3
"class inheritance"


class MyList(list):
    "Instance of a list class"
    pass

    def __init__(self):
        "initiating the class"
        super().__init__()

    def print_sorted(self):
        "function to print sorted list"
        print(sorted(self))
