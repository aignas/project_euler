#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Project Euler solution

    Problem 21: Amicable numbers



    Let d(n) be defined as the sum of proper divisors of n (numbers less than n
    which divide evenly into n).

    If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
    and each of a and b are called amicable numbers.

    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
    55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4,
    71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.


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

from functools import reduce


def factor_list(limit):
    """Get the list of factors up until (and including) a number.

    >>> all_factors = factor_list(28)
    >>> all_factors[9]
    [2, 5]
    >>> all_factors[6]
    [7]

    """
    prime_sieve = [True] * limit
    factors = [[] for i in prime_sieve]

    # Sieve through the number 1 first
    prime_sieve[0] = False

    sq_limit = int(limit**0.5)

    for p, is_prime in enumerate(prime_sieve, start=1):
        if is_prime:
            # Because of the properties of the sieve, we need to go only
            # until the square root of the limit
            if p > sq_limit:
                break

            for j in range(2 * p - 1, limit, p):
                prime_sieve[j] = False

    for p, is_prime in enumerate(prime_sieve, start=1):
        if is_prime:
            for j in range(p - 1, limit, p):
                factors[j].append(p)

    return factors


def multiplicity(n, factor):
    """Calculate the multiplicity.
    """
    if n == 1:
        return 1

    mult = 0
    while n % factor == 0:
        mult += 1
        n //= factor

    return mult


def proper_divisor_sum(n, factors):
    """Generate divisors of a number

    Examples:
        >>> all_factors = factor_list(300)
        >>> for i in [1, 2, 28, 220, 284]:
        ...     print(all_factors[i - 1])
        []
        [2]
        [2, 7]
        [2, 5, 11]
        [2, 71]

        >>> for i in [1, 2, 28, 220, 284]:
        ...     print([multiplicity(i, f) for f in all_factors[i - 1]])
        []
        [1]
        [2, 1]
        [2, 1, 1]
        [2, 1]

        >>> for i in [1, 2, 28, 220, 284]:
        ...     print(proper_divisor_sum(i, all_factors[i - 1]))
        0
        1
        28
        284
        220

    """
    if n == 1:
        return 0

    s = 0

    # First, get all the factors and multiplicity.
    mult = [multiplicity(n, f) for f in factors]

    nfactors = len(factors)
    f = [0] * nfactors
    while True:
        # First generate a list where we raise all of the factors to the
        # power of f and then we do a reduce
        s += reduce(lambda x, y: x*y,
                    [factors[x]**f[x] for x in range(nfactors)], 1)

        # FIXME: What does the following do?
        for i in range(nfactors):
            f[i] += 1
            if f[i] <= mult[i]:
                break

            f[i] = 0
        else:
            return s - n


from collections import defaultdict


def solution():
    """The solution to the problem

    """
    N = 10000
    all_factors = factor_list(N)

    # Find sums of factors:
    sums = [proper_divisor_sum(n, factors)
            for n, factors in enumerate(all_factors, start=1)]

    assert sums[283] == 220

    # Find values, which are the same in the list:
    r = []
    for i, j in enumerate(sums, start=1):
        if j in range(2, N) and i == sums[j - 1] and i != j:
            r.append(i)

    return sum(r)


def main():
    """The main function
    """
    print(benchmark(solution))


if __name__ == "__main__":
    import doctest
    if doctest.testmod()[0] == 0:
        main()
