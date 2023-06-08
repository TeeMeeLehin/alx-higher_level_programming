#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = len(argv) - 1
    index = 1
    sum = 0
    if (args == 0):
        print(args)
    elif (args == 1):
        print(argv[index])
    else:
        while (index <= args):
            sum += int(argv[index])
            index += 1
        print(sum)
