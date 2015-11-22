#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Project Euler solution

    Problem 23: Non-abundant sums



    A perfect number is a number for which the sum of its proper divisors is
    exactly equal to the number. For example, the sum of the proper divisors of
    28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
    number.

    A number n is called deficient if the sum of its proper divisors is less
    than n and it is called abundant if this sum exceeds n.

    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
    number that can be written as the sum of two abundant numbers is 24. By
    mathematical analysis, it can be shown that all integers greater than 28123
    can be written as the sum of two abundant numbers. However, this upper
    limit cannot be reduced any further by analysis even though it is known
    that the greatest number that cannot be expressed as the sum of two
    abundant numbers is less than this limit.

    Find the sum of all the positive integers which cannot be written as the
    sum of two abundant numbers.


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


from solution021 import proper_divisor_sum
from solution021 import factor_list

from itertools import combinations_with_replacement

def solution():
    """The solution to the problem
    """
    limit = 28123
    all_factors = factor_list(limit - 12)
    abundant_numbers = [
        n for n, factors in enumerate(all_factors, start=1)
        if proper_divisor_sum(n, factors) > n]

    assert 12 in abundant_numbers

    all_sums = set(
        sum(c) for c in combinations_with_replacement(abundant_numbers, 2))

    return sum(i for i in range(1, limit) if i not in all_sums)


def main():
    """The main function
    """
    print(benchmark(solution))


if __name__ == "__main__":
    import doctest
    if doctest.testmod()[0] == 0:
        main()
