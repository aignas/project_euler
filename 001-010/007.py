#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def is_prime(n, primes):
    for p in primes:
        if n % p == 0:
            return False

    return True


def get_prime(a):
    primes = [2, 3]
    number = 5
    s = -1

    while len(primes) < a:
        if is_prime(number, primes):
            primes.append(number)
        elif s == -1:
            s = 1
            number += s
        else:
            s = -1
            number += 4

    return primes[a - 1]

print(get_prime(10001))
