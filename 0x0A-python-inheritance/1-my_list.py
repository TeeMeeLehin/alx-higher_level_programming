#!/usr/bin/python3
"class inheritance"


class MyList(list):
    "Instance of a list class"
    pass

    def print_sorted(self):
        new_list = sorted(self)
        print(new_list)
