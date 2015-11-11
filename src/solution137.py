#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Project Euler 137

Question:
    Fibonacci golden nuggets.
"""

from math import sqrt, log


def A(x):
    """This is the function, which can be expressed as

        A(x) = sum(fib(k) * x**k)

    This has been derived by using the fact that the sum is infinite and
    that the Fibonacci terms can be expanded by using the recursive
    relationship.

    Test the function, so that we now, that it returns the correct
    values for the nuggets.
            √2−1       1
            1/2         2
            (√13−2)/3  3
            (√89−5)/8  4
            (√34−3)/5  5

    >>> from numpy import round
    >>> [round(A(i)) for i in
    ...  [sqrt(2) - 1,
    ...   0.5,
    ...  (sqrt(13) - 2)/3,
    ...  (sqrt(89) - 5)/8,
    ...  (sqrt(34) - 3)/5]]
    [1.0, 2.0, 3.0, 4.0, 5.0]

    """
    return x / (1 - x - x**2)


def nugget(n):
    """This will return the nugget, which is a solution to an equation:

        A(x) - n = 0

    where n is a positive integer. Since this is a quadratic equation,
    there are two roots, but we are going to discard one which does not
    satisfy the conditions.

    >>> nugget(2)
    0.5


    """
    tmp = (n + 1) / (2 * n)
    root_discriminant = sqrt(tmp**2 + 1)
    return -tmp + root_discriminant


def check_square(integer):
    """Checks whether the number is square of an integer or not.

    >>> check_square(25)
    True

    >>> check_square(24)
    False

    >>> check_square(26)
    False

    """
    return int(integer**0.5)**2 == integer


def rational_roots(number_of_roots):
    """This will return rational roots to the equation.

    >>> a = iter(rational_roots(10))
    >>> next(a)
    2
    >>> next(a)
    15

    """
    n = 1
    k = 1
    j = 0

    while j < number_of_roots:
        check = 4 + (5 * n + 1)**2

            # FIXME: I still need to check if  the resultant x is
            # rational!
            print(j, n)
            j = j + 1

        n = n + 1


def solution():
    """Main solution

    """
    return rational_roots(15)


def main(benchmark=False):
    """Main loop

    Sum of the digits.

    """
    from timeit import default_timer as timer

    start = timer()
    answer = solution()
    end = timer()
    if benchmark:
        print("Completed in: {}".format(end - start))
    return answer


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(main(True))
