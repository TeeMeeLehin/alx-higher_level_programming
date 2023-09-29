#!/usr/bin/python3
"""
Python script to solve ALXSE technical challenge
The script displays the last 10 github commtis
of a given repo.
"""

import sys
import requests

if __name__ == "__main__":

    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"
    response = requests.get(url)
    response = response.json()

    for item in response[:10]:
        sha = item.get("sha")
        author = item.get("commit").get("author").get("name")
        print(f"{sha}: {author}")
