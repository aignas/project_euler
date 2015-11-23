#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Project Euler solution

    Problem 387: Harshad Numbers



    A Harshad or Niven number is a number that is divisible by the sum of its
    digits.

    201 is a Harshad number because it is divisible by 3 (the sum of its
    digits.)

    When we truncate the last digit from 201, we get 20, which is a Harshad
    number.

    When we truncate the last digit from 20, we get 2, which is also a Harshad
    number.

    Let's call a Harshad number that, while recursively truncating the last
    digit, always results in a Harshad number a right truncatable Harshad
    number.

    Also:

    201/3=67 which is prime.

    Let's call a Harshad number that, when divided by the sum of its digits,
    results in a prime a strong Harshad number.

    Now take the number 2011 which is prime.

    When we truncate the last digit from it we get 201, a strong Harshad number
    that is also right truncatable.

    Let's call such primes strong, right truncatable Harshad primes.

    You are given that the sum of the strong, right truncatable Harshad primes
    less than 10000 is 90619.

    Find the sum of the strong, right truncatable Harshad primes less than
    1014.


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


def is_harshad_number(n):
    """Check that a number is a Harshad number

    >>> is_harshad_number('201')
    True
    >>> is_harshad_number('20')
    True
    >>> is_harshad_number('2')
    True

    """
    return int(n) % sum(int(i) for i in n) == 0


def is_right_trunc_harshad_number(n):
    """Check that a number is a Harshad number

    >>> is_right_trunc_harshad_number('201')
    True

    """
    return all(is_harshad_number(n[:i]) for i in range(1, len(n) + 1))


def find_all_rthns(limit):
    """Find all right-truncatable-Harshard numbers. 

    >>> find_all_rthns(10000)    # doctest: +NORMALIZE_WHITESPACE
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 18, 20, 21, 24, 27, 30, 36, 40,
    42, 45, 48, 50, 54, 60, 63, 70, 72, 80, 81, 84, 90, 100, 102, 108,
    120, 126, 180, 200, 201, 204, 207, 209, 210, 216, 240, 243, 247,
    270, 300, 306, 308, 360, 364, 400, 402, 405, 407, 408, 420, 423,
    450, 480, 481, 486, 500, 504, 506, 540, 600, 603, 605, 630, 700,
    702, 704, 720, 800, 801, 803, 804, 810, 840, 846, 900, 902]
    """
    return [i for i in range(1, limit)
            if is_right_trunc_harshad_number(str(i))]


def get_primes_from_chunk(start, end, primes):
    """Get all prime numbers from a chunk.
    """
    sieve = (end - start + 1) // 2 * [True]
    stop = end ** 0.5

    # If start is not one, we need to 
    if start == 1:
        sieve[0] = False
    else:
        for p in primes:
            # The id for the sieve calculation here is a bit complex.
            # 
            # The first number that is divisble by p is given by:
            # Get the last multiple:
            last_m = start // p * p

            # Now get the first multiple in the range
            if last_m % 2 == 0:
                last_m += p
            else:
                last_m += 2 * p

            # Convert to id:
            i = (last_m - start) // 2

            for j in range(i, len(sieve), p):
                sieve[j] = False

    for i, (p, is_prime) in enumerate(zip(range(start, end + 1, 2), sieve)):
        if is_prime:
            if p > stop:
                break
            
            for j in range(i + p, len(sieve), p):
                sieve[j] = False

    for p, is_prime in zip(range(start, end + 1, 2), sieve):
        if is_prime:
            primes.add(p)


def get_primes(limit):
    """Get all the primes by using a chunked sieve.
    """
    chunk_size = int(min(limit, 10**7))
    number_of_chunks = limit // chunk_size

    last_chunk_size = limit % chunk_size
    if last_chunk_size != 0:
        number_of_chunks += 1

    primes = set([2])

    for chunk_number in range(number_of_chunks):
        start = chunk_number * chunk_size
        stop = start + chunk_size

        get_primes_from_chunk(start + 1, stop, primes)

    return primes


def harshad_prime_sum(limit):
    """
    >>> harshad_prime_sum(10000)
    90619
    """

    primes = get_primes(limit)

    # Sum the strong, right truncatable Harshad primes:
    S = 0

    for p in primes:
        if p < 10:
            continue

        h = str(p)[:-1]
        if is_right_trunc_harshad_number(h):
            s = sum(int(j) for j in h)
            h = int(h)

            if h % s == 0 and h // s in primes:
                S += p

    return S

def solution():
    """The solution to the problem
    """
    return harshad_prime_sum(int(10**14))


def main():
    """The main function
    """
    print(benchmark(solution))


if __name__ == "__main__":
    import doctest
    if doctest.testmod()[0] == 0:
        print("Tests passed")
        main()
