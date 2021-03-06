#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Question:


    Let smpf(n) be the smallest prime factor of n.
    smpf(91)=7 because 91=7×13 and smpf(45)=3 because 45=3×3×5.
    Let S(n) be the sum of smpf(i) for 2 ≤ i ≤ n.
    E.g. S(100)=1257.

    Find S(10^12) mod 10^9.
"""

def series_index(prime, start, end):
    """A generator index in the series of number generated by the 6k ± 1 form.

    for the prime 5 it will do the indiceses of the numbers:
        25, 35, 55, 65, etc
    which are:
        7, 10, 17,

    """
    if start < prime**2:
        start = prime**2
    else:
        start = (start // prime + 1) * prime

        if start % 2 == 0:
            start += prime

        if start % 3 == 0:
            start += 2 * prime

    # Calculate the skip value
    skip = (start + 2 * prime) % 3 == 0

    end = end // prime * prime
    if end %2 == 0:
        end -= prime

    if end %3 == 0:
        end -= 2 * prime

    # Calculate the value needed during the iteration
    big = prime + (prime + 1)// 6 * 2
    small = prime - (prime + 1)// 6 * 2
    stop = end //2 - (end //3 - end // 6) - 1
    index = start // 2 - (start // 3 - start // 6) - 1

    while index <= stop:
        yield index
        index += big if skip else small
        skip = not skip

def series(end, end2=None):
    """A generator for generating numbers of form: 6k ± 1

    5, 7, 11, 13, 17

    """
    start = 5
    if end2 is not None:
        start, end = end, end2

    big = 4
    small = 2

    if start % 2 == 0:
        start += 1

    if start % 3 == 0:
        start += 2

    skip = (start + small) % 3 == 0
    index = start // 2 - (start // 3 - start // 6) - 1
    value = start

    while value <= end:
        yield (index, value)
        value += big if skip else small
        skip = not skip
        index += 1

def primes(limit):
    """A generator for prime numbers.

    Return prime numbers
    """
    limit = int(limit)
    number_of_evens = limit // 2
    number_of_factors_of_three = (limit + 3) // 6
    rest = limit - 1 - number_of_evens - number_of_factors_of_three

    sieve = [True] * rest

    yield 2
    yield 3

    for index, prime in series(limit):
        if sieve[index]:
            yield prime
            for index_no_prime in series_index(prime, 0, limit):
                sieve[index_no_prime] = False

class SmpfSum:
    """The class, which is calculating the smpf sum.
    """
    def __init__(self, limit):
        self.__limit = limit
        self.__primes = list(primes(limit**.5))

        # This is for storring things:
        self.factor_sum = [0] * len(self.primes)
        self.count_of_smpf = [0] * len(self.primes)

        self.count_hashmap = {}

        # First calculate the sum of 
        self.calc_smpf_count()
        self.smpf_difference()

    @property
    def primes(self):
        """The list of prime numbers
        """
        return self.__primes

    @property
    def limit(self):
        """Limit of the series
        """
        return self.__limit

    def factor_sum_calc(self, index, limit, sum_=0):
        ''' A helper
        '''
        sum_ = (limit + 1) * limit // 2
        for i in range(index):
            sum_ -= self.factor_sum_calc(i, limit // self.primes[i], sum_)

        return sum_ * self.primes[index]

    def smpf_difference(self):
        '''
        This is the number of numbers which are prime or whose smpf >=
        self.primes[i].

        '''
        for i in range(len(self.factor_sum)):
            self.factor_sum[i] = \
                self.factor_sum_calc(i, self.limit // self.primes[i])
            self.factor_sum[i] -= self.primes[i] * (1 + self.count_of_smpf[i])

    def calc_smpf_count(self):
        """This returns the number of smpfs equal to self.primes[index]

        The count can be calculated by a recursive function:

        def count(limit, i):
            if i == 0:
                return limit - 1
            else:
                return count(limit, i - 1) \
                    - count(limit // primes[i] - 1, i - 1) \
                    - count(primes[i] - 1, i - 1)

        However, this will make me run out of stack very quickly,
        hence, I should be using generators to calculate all of the
        combinations of products of the primes and then combine the
        results.  This apporoach is similar to the MapReduce used in
        Big Data.

        One possible algorithm is to:

            1. Calculate the i=0 case for limit and all
                (limit div prime_product_combination) and the
                all cases where prime - 1 = limit

            2. Sum the terms in the list

            3. Repeat that until we go through all the prime numbers

        Another:

            1. Go through the tree of functions and add instructions as
                to what values of the functions above will be needed.

            2. Then use a loop to go through the operations.

        However, this more looks like just trying to store the stack
        space somewhere else...
        """

        def count(limit, i):
            if i == 0:
                return limit - 1
            else:
                return count(limit, i - 1) \
                    - count(limit // self.primes[i] - 1, i - 1) \
                    - count(self.primes[i] - 1, i - 1)

        count_stack = []

    def get_sum(self):
        """Return the actual sum
        """
        return (self.limit + 2) * (self.limit - 1) // 2 - sum(self.factor_sum)

def solution():
    """
    Solution to the problem.
    """
    s = SmpfSum(6 * 10**3)
    hashmap_list = list(s.count_hashmap.keys())
    hashmap_list.sort()
    print(hashmap_list)
    return s.get_sum()

def main():
    """ The main function

    """
    from time import time
    start = time()
    answer = solution()
    print("Answer is: {}".format(answer))
    print("Solved in {:.3f}s".format(time() - start))

if __name__ == "__main__":
    main()
