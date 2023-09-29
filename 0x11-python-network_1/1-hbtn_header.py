#!/usr/bin/python3
""" Python script that
    displays the value of the X-Request-Id
"""

import sys
import urllib.request

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    print(response.headers.get('X-Request-Id'))
