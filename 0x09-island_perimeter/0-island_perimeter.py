#!/usr/bin/python3
"""module to check island perimeter"""

def check(grid, x, y):
    """checks the surrounding area and returns perimeter per block"""
    b_perimeter = 0
    if grid[y][x] == 1:
        if grid[y][x + 1] == 0:
            b_perimeter += 1
        if grid[y][x - 1] == 0:
            b_perimeter += 1
        if grid[y + 1][x] == 0:
            b_perimeter += 1
        if grid[y - 1][x] == 0:
            b_perimeter += 1
    return b_perimeter


def island_perimeter(grid):
    """calculates the perimeter of the grid occupied by 1s"""
    perimeter = 0

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            perimeter += check(grid, x, y)
    return perimeter
