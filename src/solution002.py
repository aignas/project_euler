#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Fin the sum of even-valued terms in the sequence, whose members do not
exceed 4 million

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
"""

def fibonacci(n):
    """
    Return the nth member of the fibonacci sequence.

    1, 2, 1 + 2, 2 + (1 + 2), (1 + 2) + (2 + (1+2)), ..
    """
    ret = 0
    last = [1, 2]
    for i in range(1, n + 1):
        if i in [1, 2]:
            ret = i
        else:
            ret = sum(last)

        last = [last[1], ret]

    return ret


def even_sum():
    sum_ = 0
    f = 1
    for i in range(2, 10**6, 3):
        member = fibonacci(i)
        if member < 4 * 10**6:
            sum_ += member
        else:
            return sum_

print(fibonacci(3))
print(fibonacci(4))
print(even_sum())
