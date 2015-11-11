#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Project Euler 25.

Question:
    n! means n × (n − 1) × ... × 3 × 2 × 1

    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
    and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0
    + 0 = 27.

    Find the sum of the digits in the number 100!
"""


def factorial(number):
    """Factorial function

    >>> factorial(10)
    3628800

    """
    answer = 1
    while number:
        answer *= number
        number -= 1

    return answer


def main(args, benchmark=False):
    """Main loop

    Sum of the digits.

    >>> main(10)
    27

    """
    from timeit import default_timer as timer

    start = timer()
    answer = sum(int(i) for i in str(factorial(args)))
    end = timer()
    if benchmark:
        print("Completed in: {}".format(end - start))
    return answer


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(main(100, True))
