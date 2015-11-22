#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Project Euler solution

    Problem 27: Quadratic primes



    Euler discovered the remarkable quadratic formula:

    n² + n + 41

    It turns out that the formula will produce 40 primes for the consecutive
    values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41
    is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly
    divisible by 41.

    The incredible formula  n² − 79n + 1601 was discovered, which produces 80
    primes for the consecutive values n = 0 to 79. The product of the
    coefficients, −79 and 1601, is −126479.

    Considering quadratics of the form:



    n² + an + b, where |a| < 1000 and |b| < 1000where |n| is the
    modulus/absolute value of ne.g. |11| = 11 and |−4| = 4



    Find the product of the coefficients, a and b, for the quadratic expression
    that produces the maximum number of primes for consecutive values of n,
    starting with n = 0.


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


from solution035 import get_primes


def solution():
    """The solution to the problem
    """
    primes = set(get_primes(1000000))
    m = 0
    r = 0
    for a in range(-1000, 1000):
        for b in range(-1000, 1000):
            for n in range(1000):
                p = n * n + a * n + b
                if p not in primes:
                    if n + 1 > m:
                        r = a * b
                        m = n + 1
                    break

    return r


def main():
    """The main function
    """
    print(benchmark(solution))


if __name__ == "__main__":
    import doctest
    if doctest.testmod()[0] == 0:
        main()
