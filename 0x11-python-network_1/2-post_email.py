#!/usr/bin/python3
""" Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter
and displays the responsebody
"""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}
    encoded_data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, data=encoded_data, method="POST")

    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
