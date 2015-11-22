#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Project Euler 104

Question:
    The Fibonacci sequence is defined by the recurrence relation:

        Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

    It turns out that F541, which contains 113 digits, is the first
    Fibonacci number for which the last nine digits are 1-9 pandigital
    (contain all the digits 1 to 9, but not necessarily in order). And
    F2749, which contains 575 digits, is the first Fibonacci number for
    which the first nine digits are 1-9 pandigital.

    Given that Fk is the first Fibonacci number for which the first nine
    digits AND the last nine digits are 1-9 pandigital, find k.
"""


def fib(stop=0):
    """Fibonacci sequence
    >>> [(k + 1, n) for k, n in enumerate(fib(34))]
    [(1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21), (9, 34)]

    """

    n = 1
    m = 1

    yield n
    while n <= stop or stop == 0:
        yield n
        n, m = m, n
        n = n + m


def is_pandigital(number):
    """This just checks whether the number is pandigital

    >>> is_pandigital(123456789)
    True
    >>> is_pandigital(123456787)
    False

    """
    number = str(number)
    return all(i in number for i in '1234356789')


def get_last_digits(number, number_of_digits=9):
    """This gets the last numbers of a digit
    >>> get_last_digits(12345678987654321)
    987654321
    >>> get_last_digits(1234567)
    1234567

    """
    return number % 10**number_of_digits

def get_first_digits(number, number_of_digits=9):
    """This gets the first numbers of a digit

    >>> get_first_digits(12345678987654321)
    123456789
    >>> get_first_digits(1234567)
    1234567

    """
    return int(str(number)[:number_of_digits])

def example_pandigital_last():
    """F541, which contains 113 digits,

    >>> example_pandigital_last()
    (541, 113)
    """
    for k, n in enumerate(fib()):
        if is_pandigital(get_last_digits(n)):
            return k + 1, len(str(n))

def example_pandigital_first():
    """ F2749, which contains 575 digits

    >>> example_pandigital_first()
    (2749, 575)
    """
    for k, n in enumerate(fib()):
        if is_pandigital(get_first_digits(n)):
            return k + 1, len(str(n))

def solution():
    """Main solution

    >>> solution()
    (329468, 68855)

    """
    for k, n in enumerate(fib()):
        # Skip all the cases which are not front pandigital
        if k < 2748:
            continue

        # If the number is not end-pandigital, we skip the front check
        if not is_pandigital(get_last_digits(n)):
            continue

        if is_pandigital(get_first_digits(n)):
            return k + 1, len(str(n))


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
