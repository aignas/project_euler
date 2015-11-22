#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Project Euler solution

    Problem 30: Digit fifth powers



    Surprisingly there are only three numbers that can be written as the sum of
    fourth powers of their digits:

    1634 = 14 + 64 + 34 + 44

    8208 = 84 + 24 + 04 + 84

    9474 = 94 + 44 + 74 + 44

    As 1 = 14 is not a sum it is not included.

    The sum of these numbers is 1634 + 8208 + 9474 = 19316.

    Find the sum of all the numbers that can be written as the sum of fifth
    powers of their digits.


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


def solution():
    """The solution to the problem
    """
    return sum(i for i in range(2, 1000000)
               if i == sum(int(j)**5 for j in str(i)))


def main():
    """The main function
    """
    print(benchmark(solution))


if __name__ == "__main__":
    import doctest
    if doctest.testmod()[0] == 0:
        main()
