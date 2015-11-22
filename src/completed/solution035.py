#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Project Euler solution

    Problem 35: Circular primes



    The number, 197, is called a circular prime because all rotations of the
    digits: 197, 971, and 719, are themselves prime.

    There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
    71, 73, 79, and 97.

    How many circular primes are there below one million?


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


from collections import defaultdict


def circular_perms(string, c=set):
    """A generator for circular permutations of strings. May contain duplicates

    >>> circular_perms('ABC', list)
    ['ABC', 'BCA', 'CAB']

    >>> circular_perms('ABA', list)
    ['ABA', 'BAA', 'AAB']

    >>> circular_perms('AA', list)
    ['AA', 'AA']

    """
    return c(string[i:] + string[:i] for i in range(len(string)))


def get_primes(limit):
    """Get the list of primes up until a number.

    """
    sieve = [True] * (limit // 2)

    # Sieve through the number 1 first
    sieve[0] = False

    sq_limit = int(limit**0.5)

    for i, is_prime in enumerate(sieve):
        if is_prime:
            p = 2 * i + 1

            # Because of the properties of the sieve, we need to go only
            # until the square root of the limit
            if p > sq_limit:
                break

            for j in range(i + p, len(sieve), p):
                sieve[j] = False

    # Now, populate the lists:
    return [2] + [
        2 * i + 1 for i, is_prime in enumerate(sieve) if is_prime]


def solution(limit=10**6):
    """The solution to the problem

    >> solution(limit=100)
    13

    [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]

    This solves the given problem in about 0.139 seconds, which in my
    opinion is good enough. :)
    """
    primes = [str(i) for i in get_primes(limit)]

    ret = 0

    prime_sets = defaultdict(set)
    gone_through = defaultdict(set)
    circular_sets = defaultdict(set)

    # Categorize the primes
    for p in primes:
        # Check if the number has 0, 2, 4, 5, 6, 8 as then one cyclical
        # permutation will not be a prime. Also, a genexp here would be
        # really nice, but this might be faster.
        if len(p) > 1 and ('0' in p or '2' in p or '4' in p or '5' in p or
                           '6' in p or '8' in p):
            continue

        label = ''.join(sorted(p))
        prime_sets[label].add(p)

    # Now, count the number of circular primes:
    for label, permutation_set in prime_sets.items():
        # Go through each permutation_set and check if the circular set
        # is a subset of the permutation number itself.
        for item in permutation_set:

            # Do not build permutation lists twice for the same item
            if item in gone_through[label]:
                continue

            # FIXME: This is called to often!
            circle = circular_perms(item)
            gone_through[label] |= circle

            # Check if a newly constructed set is a subset
            if circle <= permutation_set:
                circular_sets[label] |= circle

    ret = sum(len(s) for s in circular_sets.values())

    return ret


def main():
    """The main function
    """
    print(benchmark(solution))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
