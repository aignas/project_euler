#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Project Euler solution

    Problem 31: Coin sums



    In England the currency is made up of pound, £, and pence, p, and there are
    eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

    It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

    How many different ways can £2 be made using any number of coins?


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


def solution():
    """The solution to the problem

    I am given divisors of 200 and I need to say how many ways are there
    to produce the number 200.
    """
    target = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]

    m = [200, 100, 40, 20, 4, 2, 1]
    c = [0] * len(coins)

    C = 1

    i = 1
    while c[-1] != 1:
        c[i] = m[i]
        while m[i] != 0:
            m[i] -= 1


    for i in 

    return C


def main():
    """The main function
    """
    print(benchmark(solution))


if __name__ == "__main__":
    import doctest
    if doctest.testmod()[0] == 0:
        main()
