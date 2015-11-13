
#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Project Euler solution

    Problem 26: Reciprocal cycles



    A unit fraction contains 1 in the numerator. The decimal representation of
    the unit fractions with denominators 2 to 10 are given:



    1/2= 0.5

    1/3= 0.(3)

    1/4= 0.25

    1/5= 0.2

    1/6= 0.1(6)

    1/7= 0.(142857)

    1/8= 0.125

    1/9= 0.(1)

    1/10= 0.1



    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can
    be seen that 1/7 has a 6-digit recurring cycle.

    Find the value of d < 1000 for which 1/d contains the longest recurring
    cycle in its decimal fraction part.


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
    pass


def main():
    """The main function
    """
    # benchmark(solution)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
