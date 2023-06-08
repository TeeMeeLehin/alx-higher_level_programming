#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = len(argv) - 1
    index = 1
    if (args == 0):
        print("{} arguments.".format(args))
    elif (args == 1):
        print("{} argument:".format(args))
        print("{}: {}".format(index, argv[index]))
    else:
        print("{} arguments:".format(args))
        while (index <= args):
            print("{}: {}".format(index, argv[index]))
            index += 1
