#!/usr/bin/python3
"creating a pascal triangle"


def pascal_triangle(n):
    "function"
    if n <= 0:
        return []
    triangle = [[1]]
    while len(triangle) != n:
        last_t = triangle[-1]
        tmp = [1]
        for i in range(len(last_t) - 1):
            tmp.append(last_t[i] + last_t[i + 1])
        tmp.append(1)
        triangle.append(tmp)
    return triangle
