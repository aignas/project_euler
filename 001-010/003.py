#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def factorize(n):
    factors = set()
    factor = 2
    sq = n**0.5
    while n > 1:
        if n % factor == 0:
            factors.add(factor)
            while n % factor == 0:
                n = n // factor
            sq = n**.5
        elif sq < factor:
            # The n cannot have a factor which is larger than it's
            # square root. That is, if we have factored out all the
            # lower factors already.
            factors.add(n)
            break
        else:
            # Because we have already excluded all even factors, we can
            # increment the factor by 2
            if factor == 2:
                factor = 3
            else:
                factor += 2

    return factors

print(factorize(13195))
print(factorize(600851475143))
