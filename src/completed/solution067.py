#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Project Euler solution

    Problem 67: Maximum path sum II



    By starting at the top of the triangle below and moving to adjacent numbers
    on the row below, the maximum total from top to bottom is 23.

    37 4

    2 4 6

    8 5 9 3

    That is, 3 + 7 + 4 + 9 = 23.

    Find the maximum total from top to bottom in triangle.txt (right click and
    'Save Link/Target As...'), a 15K text file containing a triangle with one-
    hundred rows.

    NOTE: This is a much more difficult version of Problem 18. It is not
    possible to try every route to solve this problem, as there are 299
    altogether! If you could check one trillion (1012) routes every second it
    would take over twenty billion years to check them all. There is an
    efficient algorithm to solve it. ;o)


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
    with open('problem067.txt', 'r') as file_:
        array = [[int(j) for j in i.strip().split()]
                 for i in file_.readlines()]

        for i in range(len(array) - 2, -1, -1):
            for j in range(len(array[i])):
                array[i][j] += max(array[i+1][j], array[i+1][j+1])

        return array[0][0]


def main():
    """The main function
    """
    print(benchmark(solution))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
