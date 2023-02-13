#!/usr/bin/python3
"""rotate 2D matrix module"""

def rotate_2d_matrix(matrix):
    """function takes an n x n array and rotates it by 90 degree"""
    temp_matrix = [arr.copy() for arr in matrix]
    size = len(matrix)
    row_index = 0

    for i in range(size):
        temp_row = []

        for j in range(size - 1, -1, -1):
            temp_row.append(temp_matrix[j][i])

        for k in range(size):
            matrix[row_index][k] = temp_row[k]
        row_index += 1

