#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Project Euler solution

    Problem 19: Counting Sundays

    You are given the following information, but you may prefer to do some
    research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.

    A leap year occurs on any year evenly divisible by 4, but not on a century
    unless it is divisible by 400.

    How many Sundays fell on the first of the month during the twentieth
    century (1 Jan 1901 to 31 Dec 2000)?

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

import datetime

def solution():
    """The solution to the problem
    """
    start = datetime.date(1901, 1, 1)
    end = datetime.date(2000, 12, 31)

    # Go to the first Sunday:
    start += datetime.timedelta(days=(6 - start.weekday()))

    assert start.weekday() == 6, \
        "Should have got 6, but got %d" % start.weekday()

    # Instantiate a week time delta
    week = datetime.timedelta(weeks=1)

    count = 0
    while start.year <= 2000:
        if start.day == 1:
            count += 1

        start += week

    return count


def main():
    """The main function
    """
    print(benchmark(solution))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
