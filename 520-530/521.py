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

def series_gen(n):
    """
    5, 7, 11, 13, 17
    """
    i = -1
    k = 1
    m = 6*k + i
    while n > m:
        yield m
        if i == 1:
            k += 1
        i = -i
        m = 6*k + i

def S(n, mod=-1):
    """
    Number of terms in the sum are: n - 1
    Number of terms equal to 2 are: n//2

    Then we can use a table of primes.
    """
    primes = [5]

    # Add to the sum all the even number primes
    sum_ = n//2*2
    sum_ += (n - n//2*2 - 1)//3*3

    # odd number smpfs numbers
    # Check the smpf in a list of primes!
    for i in series_gen(n):
        sq = i**0.5
        for k in primes:
            if i % k == 0:
                sum_ += k
                break

            if k > sq:
                primes.append(i)
                sum_ += i
                break

    return sum_

def test_solution():
    print(list(series_gen(20)))
    result = S(100)
    assert result == 1257, "Got %d" % result
    result = S(101)
    assert result == 1358, "Got %d" % result

def solution():
    """
    Solution to the problem.
    """
    test_solution()
    return S(100)


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
