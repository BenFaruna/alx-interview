#!/usr/bin/python3
"""
Pascal Triangle using python
"""

def find_factorial(i):
    """function to find factorial"""
    if i == 1 or i == 0:
        return 1
    else:
        return i * find_factorial(i - 1)

def factorial_formula(n, k):
    """function of combination formula"""
    return int(find_factorial(n) / (find_factorial(n - k) * find_factorial(k)))

def pascal_triangle(num):
    """return the pascal triangle for a given range num"""
    triangle = []
    for n in range(num):
        row = []
        for k in range(n + 1):
            row.append(factorial_formula(n, k))
        triangle.append(row)

    return triangle

