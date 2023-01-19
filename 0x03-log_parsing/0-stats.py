#!/usr/bin/python3
import sys
"""module reads stdin and computes metric"""

def print_stats(size: int, status_code: dict) -> None:
    """prints file and count of all status codes"""
    print("File size: {}".format(file_size))
    for code, count in status_code.items():
        print("{}: {}".format(code, count))


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
        if 9 == len(line_n):
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