
#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Project Euler solution

    Problem 9: Special Pythagorean triplet



    A Pythagorean triplet is a set of three natural numbers, a < b < c, for
    which,

     a^2 + b^2 = c^2

    For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

    There exists exactly one Pythagorean triplet for which a + b + c =
    1000.Find the product abc.


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
    """
    N = 1000
    P_correct = 0
    for a in range(1, 999):
        for b in range(a + 1, 999):
            c = N - a - b
            if c < 0:
                continue

            if not (c > b > a):
                break
            
            if c**2 == a**2 + b**2:
                P_correct = a * b * c

    return P_correct


def main():
    """The main function
    """
    print(benchmark(solution))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
