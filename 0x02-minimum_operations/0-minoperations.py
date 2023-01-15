#!/usr/bin/python3
###minimum operations"""


def minOperations(n: int):
    """return fewest number of operations needed to copy n h(s)"""
    min = 0

    while n != 0:
        if n % 2 == 0:
            min += 1
            n /= 2
        else:
            min += 1
            n -= 1

    return min
