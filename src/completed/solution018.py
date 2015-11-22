#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Project Euler solution

    Problem 18: Maximum path sum I



    By starting at the top of the triangle below and moving to adjacent numbers
    on the row below, the maximum total from top to bottom is 23.

    3
    7 4
    2 4 6
    8 5 9 3

    That is, 3 + 7 + 4 + 9 = 23.

    Find the maximum total from top to bottom of the triangle below:

    75
    95 64
    17 47 82
    18 35 87 10
    20 04 82 47 65
    19 01 23 75 03 34
    88 02 77 73 07 63 67
    99 65 04 28 06 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

    NOTE: As there are only 16384 routes, it is possible to solve this problem
    by trying every route. However, Problem 67, is the same challenge with a
    triangle containing one-hundred rows; it cannot be solved by brute force,
    and requires a clever method! ;o)


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


def triangle_solution(triangle):
    """The actual function which does the work by iterating over each
    possible path.

    The outline of the algorithm:

    1. Start with the bottom of the triangle and find the highest numbers.
    2. Go to the row above and find the highest sums and replace the
    nodes with the sum values.
    3. ...
    4. Once we reach the top we should arrive at a sum which is the
    largest if we select the largest sum on our way up.

    """
    array = [[int(j) for j in i.split()]
             for i in triangle.strip().split('\n')]

    number_of_possibilities = factorial(len(array[-1]))
    for i in range(len(array) - 2, -1, -1):
        for j in range(len(array[i])):
            array[i][j] += max(array[i+1][j], array[i+1][j+1])

    return array[0][0]


def test_solution():
    """
    >>> test_solution()
    23

    3 + 7 + 4 + 9 = 23.
    """
    triangle = """
    3
    7 4
    2 4 6
    8 5 9 3
    """
    return triangle_solution(triangle)


def solution():
    """The solution to the problem
    """
    triangle = """
    75
    95 64
    17 47 82
    18 35 87 10
    20 04 82 47 65
    19 01 23 75 03 34
    88 02 77 73 07 63 67
    99 65 04 28 06 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
    """
    return triangle_solution(triangle)


def main():
    """The main function
    """
    print(benchmark(solution))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
