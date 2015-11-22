#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Project Euler solution

    Problem 15: Lattice paths



    Starting in the top left corner of a 2×2 grid, and only being able to move
    to the right and down, there are exactly 6 routes to the bottom right
    corner.

    How many such routes are there through a 20×20 grid?

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


def solution(dimension=2):
    """The solution to the problem

    This is just a simple combinatorics problem. There need to be an
    equal number of down and right movements and different paths mean a
    different ordering of those vectors.

    The number of slots is the sum and there will be all slots in the
    and the order matters, because we have two types. However, if we
    permute the elements of a single type, then the order doesn't
    matter, so we need to divide by the factorial of the number of
    elements of that particular type.

    We can make interesting generalizations (e.g. for N dimensional cube):

        N = factorial(sum(dimensions)) // reduce(factorial, dimensions)

    """
    d = dimension
    r = dimension

    ret = factorial(r + d) // (factorial(r) * factorial(d))
    print(ret)
    return ret


def main():
    """The main function
    """
    benchmark(solution)
    benchmark(solution, 20)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
