#!/usr/bin/python3
"""module for making change function"""


def makeChange(coins, total):
    """return the fewest number of coins needed to meet given amount total"""
    count = 0
    coins_sort = sorted(coins, reverse=True)
    i = 0

    if total <= 0:
        return count

    while total > 0 and i < len(coins_sort):
        if total >= coins_sort[i]:
            total -= coins_sort[i]
            count += 1
        else:
            i += 1

    if total == 0:
        return count

    return -1
