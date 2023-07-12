#!/usr/bin/python3
"class inheritance"


class MyList(list):
    "Instance of a list class"
    pass

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
