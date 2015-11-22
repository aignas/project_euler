#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Project Euler solution

    Problem 25: 1000-digit Fibonacci number



    The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

    Hence the first 12 terms will be:

    F1 = 1

    F2 = 1

    F3 = 2

    F4 = 3

    F5 = 5

    F6 = 8

    F7 = 13

    F8 = 21

    F9 = 34

    F10 = 55

    F11 = 89

    F12 = 144

    The 12th term, F12, is the first term to contain three digits.

    What is the index of the first term in the Fibonacci sequence to contain
    1000 digits?


"""

def fibonacci(end):
    """This is a generator approach to the Fibonacci sequence

    >>> [i for i in fibonacci(145)]
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

    """
    # pylint: disable=invalid-name
    n = 1
    m = 1

    yield n
    while n < end:
        yield n
        n, m = m, n
        n += m
     

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
    const = 10**1000
    for i, n in enumerate(fibonacci(10**1001)):
        if n > const:
            print(i, n)
            return n


def main():
    """The main function
    """
    benchmark(solution)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
