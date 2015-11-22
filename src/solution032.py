#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Project Euler solution

    Problem 32: Pandigital products



    We shall say that an n-digit number is pandigital if it makes use of all
    the digits 1 to n exactly once; for example, the 5-digit number, 15234, is
    1 through 5 pandigital.

    The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
    multiplicand, multiplier, and product is 1 through 9 pandigital.

    Find the sum of all products whose multiplicand/multiplier/product identity
    can be written as a 1 through 9 pandigital.

    HINT: Some products can be obtained in more than one way so be sure to only
    include it once in your sum.


"""


def benchmark(func, *args, **kwargs):
    """A simple benchmark to check execution time of the code
    """
    from timeit import default_timer as timer

    start = timer()
    answer = func(*args, **kwargs)
    end = timer()
    print("Completed in: {}".format(end - start))
    return answer

from itertools import permutations


def solution():
    """The solution to the problem
    """
    for perm in permutations('123456789'):


def main():
    """The main function
    """
    print(benchmark(solution))


if __name__ == "__main__":
    import doctest
    if doctest.testmod()[0] == 0:
        main()
