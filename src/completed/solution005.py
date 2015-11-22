#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def factorize(n):
    factors = list()
    factor = 2
    sq = n**0.5
    while n > 1:
        if n % factor == 0:
            factors.append(factor)
            n = n // factor
        else:
            # Because we have already excluded all even factors, we can
            # increment the factor by 2
            if factor == 2:
                factor = 3
            else:
                factor += 2

    return factors

def get_prime_list(list_):
    r = [1, 2]
    for i in list_[2:]:
        factors = factorize(i)
        for f in set(factors):
            while r.count(f) < factors.count(f):
                r.append(f)

    return r


def smallest_multiple(k):
    factors = list(range(1, k+1))

    l = get_prime_list(factors)

    product = 1
    for i in l:
        product *= i

    return product


print(smallest_multiple(10))
print(smallest_multiple(20))
print(smallest_multiple(1000))
