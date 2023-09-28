#!/bin/bash
# Bash script displays the size of the body of URL response
curl -s "$1" | wc -c
