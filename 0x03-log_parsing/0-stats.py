#!/usr/bin/python3
""" Log parsing """
import sys


def print_stats(total_size, status_codes):
    """ Helper function. Print right format """
    codes = ["200", "301", "400",  "401", "403", "404", "405", "500"]
    print("File size: {}".format(total_size))
    for code in codes:
        if status_codes[code] != 0:
            print("{}: {}".format(code, status_codes[code]))


codes_count = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
total_size = 0
line_num = 0

try:
    for line in sys.stdin:
        words = line.split()
        if (len(words) < 2):
            continue
        line_num += 1
        total_size += int(words[-1])
        if words[-2] in codes_count:
            codes_count[words[-2]] += 1

        if (line_num % 10 == 0):
            print_stats(total_size, codes_count)
except KeyboardInterrupt:
    print_stats(total_size, codes_count)
    raise

print_stats(total_size, codes_count)