#!/usr/bin/python3
"""A script that
sends a request to the URL
and displays the value
of the X-Request-Id variable
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        print(response.headers.get("X-Request-Id"))
