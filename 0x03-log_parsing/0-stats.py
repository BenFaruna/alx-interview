#!/usr/bin/python3
"""module reads stdin and computes metric"""
import sys


def print_stats(size: int, status_code: dict) -> None:
    """prints file and count of all status codes"""
    print("File size: {}".format(file_size))
    codes = ["200", "301", "400",  "401", "403", "404", "405", "500"]
    for code in codes:
        if status_code[code] != 0:
            print("{}: {}".format(code, status_code[code]))


count = 0
file_size = 0
status_code = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for line in sys.stdin:
        line_n = line.split()
        if len(line_n) == 9:
            count += 1
            file_size = file_size + int(line_n[-1])
            code = line_n[-2]

            if code in status_code:
                status_code[code] += 1
        else:
            continue

        if count % 10 == 0:
            print_stats(file_size, status_code)
except KeyboardInterrupt:
    print_stats(file_size, status_code)
    raise
