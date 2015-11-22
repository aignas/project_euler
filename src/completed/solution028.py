#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Project Euler solution

    Problem 28: Number spiral diagonals



    Starting with the number 1 and moving to the right in a clockwise direction
    a 5 by 5 spiral is formed as follows:

    21 22 23 24 25

    20  7  8  9 10

    19  6  1  2 11

    18  5  4  3 1217 16 15 14 13

    It can be verified that the sum of the numbers on the diagonals is 101.

    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
    formed in the same way?


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


def series(limit):
    """A generator which yields sums of batches of 4 terms on the diagonals whilst going in a spiral:

        1   3   5   7
        9   13  17  21
        25  31  37  43
        49  57  65  73
        81 ...

        1                   1
        3   5   7   9
        13  17  21  25
        31  37  43  49
        57  65  73  81

    >>> it = iter(series(1001))
    >>> next(it)
    1
    >>> next(it)
    24
    >>> next(it)
    76

    >>> sum(series(5))
    101


    """
    yield 1
    u_k = 3
    d = 2
    while d < limit:
        yield 4 * u_k + 6 * d
        u_k += 4 * d + 2
        d += 2


def solution(size_of_spiral=5):
    """The solution to the problem
    """
    return sum(series(1001))


def main():
    """The main function
    """
    print(benchmark(solution))


if __name__ == "__main__":
    import doctest
    if doctest.testmod()[0] == 0:
        main()
