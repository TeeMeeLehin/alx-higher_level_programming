#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return(fct(args[0], args[1]))
    except (ValueError, TypeError, IndexError, ZeroDivisionError) as error:
        print("Exception:", error, file=sys.stderr)
        return None
