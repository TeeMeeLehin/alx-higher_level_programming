#!/bin/bash
# Bash script displays the size of the body of URL response

URL="$1"

curl -s "$URL" | wc -c
