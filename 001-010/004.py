#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def test_pal(n):
    """
    Test if the number is palindromic.
    """
    return str(n)[::-1] == str(n)


def get_largest_pal(k):
    """ Input the number of digits
    """
    min_ = 10**(k-1)
    max_ = 10**k
    largest = 0
    for i in range(max_ -1, min_, -1):
        for j in range(max_-1, i, -1):
            prod = i * j
            if test_pal(prod) and prod > largest:
                largest = prod

    return largest

print(get_largest_pal(2))
print(get_largest_pal(3))
print(get_largest_pal(4))
print(get_largest_pal(5))
