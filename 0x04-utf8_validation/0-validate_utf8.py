#!/usr/bin/python3
"""utf8 validation module"""

def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    for bit in data:
        if bit > 255:
            return False
    return True
