
#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Project Euler solution

    Problem 10: Summation of primes



    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.


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
    """ 6k+-1
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
    sum_ = 5

    for pp in possible_primes():
        limit = pp**0.5

        for p in primes:
            if p > limit:
                primes.append(pp)
                sum_ += pp
                break

            if pp % p == 0:
                break

        if primes[-1] > 2000000:
            break

    return sum_


def main():
    """The main function
    """
    print(benchmark(solution))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
