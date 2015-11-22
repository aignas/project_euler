#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Project Euler solution

    Problem 34: Digit factorials



    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

    Find the sum of all numbers which are equal to the sum of the factorial of
    their digits.

    Note: as 1! = 1 and 2! = 2 are not sums they are not included.


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


from math import factorial
from itertools import combinations_with_replacement


def solution():
    """The solution to the problem

    >>> solution()
    40730

    """
    factorials = {str(i): factorial(i) for i in range(10)}

    r = []

    for number_of_digits in range(2, 8):
        for c in combinations_with_replacement('0123456789', number_of_digits):
            sum_ = sum(factorials[i] for i in c)
            sum_str = str(sum_)

            if len(sum_str) == len(c) and sorted(sum_str) == sorted(c):
                r.append(sum_)

    print(r)
    return sum(r)


def main():
    """The main function
    """
    print(benchmark(solution))


if __name__ == "__main__":
    import doctest
    if doctest.testmod()[0] == 0:
        main()
