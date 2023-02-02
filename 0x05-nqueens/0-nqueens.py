#!/usr/bin/env python3
""" 0x0C. N Queens """
import sys


def n_queens(n):
    """main function that holds the running of n"""

    board = [0 for _ in range(n)]
    result = []

    get_result(board, result, n, 0)
    return populate_result(result, n)


def get_result(board, result, n, row):
    """function that adds queen position to the result list"""

    if row == n:
        result.append(list(board))
        return True

    for i in range(len(board)):
        if check(i, row, board):
            board[row] = i
            get_result(board, result, n, row + 1)


def check(col, row, board):
    """check queen position is same as previous position and return boolean"""

    for j in range(row):
        prev_col = board[j]
        similar_col = prev_col == col
        similar_axes = abs(col - prev_col) == abs(row - j)

        if similar_col or similar_axes:
            return False

    return True


def populate_result(result, n):
    """adds data from the result list and print"""

    for solution_index in range(len(result)):
        temp_list = []
        for col_index in range(n):
            temp_list.append([col_index, result[solution_index][col_index]])
        print(temp_list)


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

n = sys.argv[1]

try:
    n = int(n)
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

n_queens(n)
