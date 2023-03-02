#!/usr/bin/python3
""" 0x1C. Island Perimeter """


def island_perimeter(grid):
    """ 0x1C. Island Perimeter """

    perimeter = 0
    for row_index, row in enumerate(grid):
        for col_index, elem in enumerate(row):
            if elem == 1:
                if row_index == 0 or grid[row_index - 1][col_index] == 0:
                    perimeter += 1
                if row_index == len(grid) - 1 or \
                        grid[row_index + 1][col_index] == 0:
                    perimeter += 1
                if col_index == 0 or grid[row_index][col_index - 1] == 0:
                    perimeter += 1
                if col_index == len(grid[row_index]) - 1 or \
                        grid[row_index][col_index + 1] == 0:
                    perimeter += 1
    return perimeter
