
#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Project Euler solution

    Problem 7: 10001st prime



    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
    that the 6th prime is 13.

    What is the 10 001st prime number?


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


def possible_primes():
    """A generator which returns 6k +/- 1
    """
    n = 5
    while True:
        yield n
        n += 2
        yield n
        n += 4


def solution():
    """The solution to the problem
    """
    primes = [2, 3]
    D = 10001

    for pp in possible_primes():
        if len(primes) == D:
            return primes[-1]

        limit = pp**0.5

        for p in primes:
            if p > limit:
                primes.append(pp)
                break

            if pp % p == 0:
                break


def main():
    """The main function
    """
    print(benchmark(solution))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
