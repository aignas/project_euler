#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Solves in 6.458s and in 0.580s with PyPy.
"""


def main():
    """ The main function

    primes can be written as 6k +/- 1
    to check wether the number is a prime, we check whether the number
    is divisible by any prime already in the list.

    """
    thresh = 2e6
    k = 1
    n = -1
    number = 6 * k + n
    primes = []
    sum_ = 2 + 3 + sum(primes)
    while number < thresh:
        is_prime = True
        sq = number**0.5
        for p in primes:
            if number % p == 0:
                is_prime = False
                break
            elif sq < p:
                break

        if is_prime:
            primes.append(number)
            sum_ += number

        if n == -1:
            n = 1
        else:
            n = -1
            k += 1

        number = 6 * k + n

    print("Sum of primes less than %d: %d" % (thresh, sum_))

if __name__ == "__main__":
    import time
    start = time.time()
    main()
    print("Exec time: %.3f" % (time.time() - start))
