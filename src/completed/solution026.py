#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Project Euler solution

    Problem 26: Reciprocal cycles



    A unit fraction contains 1 in the numerator. The decimal representation of
    the unit fractions with denominators 2 to 10 are given:



    1/2= 0.5

    1/3= 0.(3)

    1/4= 0.25

    1/5= 0.2

    1/6= 0.1(6)

    1/7= 0.(142857)

    1/8= 0.125

    1/9= 0.(1)

    1/10= 0.1



    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can
    be seen that 1/7 has a 6-digit recurring cycle.

    Find the value of d < 1000 for which 1/d contains the longest recurring
    cycle in its decimal fraction part.


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


from collections import deque


def periodic_frac(n, print_fraction=False):
    '''Returns the periodic fraction string which is equal to 1/n.

    Args:
        n (int): denominator.

    >>> periodic_frac(3, True)
    Fraction: '0.(3)'
    1

    >>> periodic_frac(6, True)
    Fraction: '0.1(6)'
    1

    >>> periodic_frac(5, True)
    Fraction: '0.2'
    0

    >>> periodic_frac(7, True)
    Fraction: '0.(142857)'
    6

    >>> periodic_frac(11, True)
    Fraction: '0.(09)'
    2

    '''
    """
1. Initial number is 1.
2. The remainder set is empty.
3. The decimal representation is empty.
4. While the remainder is not in the remainder set do:
    a. Divide by the number
    b. If it does not divide:
        i.jjj

    """

    decimal = []
    remainders = set([1])
    N = 1

    while True:
        N *= 10
        k = N // n
        decimal.append(k)

        if k != 0:
            N %= n
            if N == 0 or N in remainders:
                break
            remainders.add(N)

    if N == 0:
        if print_fraction:
            print("Fraction: '0.{}'".format(
                ''.join([str(i) for i in decimal])))
        return 0
    else:
        start_of_repeating = decimal.index(N * 10 // n)
        if print_fraction:
            print("Fraction: '0.{}({})'".format(
                ''.join([str(i) for i in decimal[:start_of_repeating]]),
                ''.join([str(i) for i in decimal[start_of_repeating:]])))
        return len(decimal) - start_of_repeating



def solution():
    """The solution to the problem

    The idea here is that any f
    """
    fractions = [periodic_frac(i) for i in range(2, 1000)]
    return fractions.index(max(fractions)) + 2


def main():
    """The main function
    """
    print(benchmark(solution))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
