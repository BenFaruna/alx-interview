#!/usr/bin/python3
"""utf8 validation module"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    flag_num = 0

    if len(data) == 0:
        return True

    for elem in data:
        b_elem = '{0:08b}'.format(elem)[-8:]
        if flag_num == 0:
            len_num = 0
            for digit in b_elem:
                if digit == "1":
                    len_num += 1
                else:
                    break
                if len_num > 4:
                    return False
            if len_num == 1:
                return False
            if len_num != 0:
                flag_num = 1
                len_num -= 1
        else:
            if b_elem[:2] != "10":
                return False
            len_num -= 1
            if len_num == 0:
                flag_num = 0

    if len_num > 0:
        return False

    return True
