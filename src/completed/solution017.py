#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Project Euler solution

    Problem 17: Number letter counts



    If the numbers 1 to 5 are written out in words: one, two, three, four,
    five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written out
    in words, how many letters would be used?

    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
    forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
    20 letters. The use of "and" when writing out numbers is in compliance with
    British usage.

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


import inflect
import re
P = inflect.engine()


def solution(limit=5):
    """The solution to the problem

    >>> solution()
    19
    """

    units = [''] + 'one two three four five six seven eight nine'.split()
    tens = [''] + (
        'ten twenty thirty forty fifty sixty seventy eighty ninety').split()
    teens = [''] + (
        'eleven twelve thirteen fourteen fifteen sixteen '
        'seventeen eighteen nineteen').split()
    thousands = [''] + (
        'thousand million billion').split()

    ret = 0

    if limit % 10 != 0:
        ret += sum(len(units[i + 1]) for i in range(limit % 10))
    elif limit == 1000:
        # Add the 'one thousand'
        c = 1
        ret += len('one')
        ret += len('thousand')

        # Add all numbers which are between 1 and 99
        a = sum([
            # Add all units
            sum(len(i) for i in units),
            # Add all teens
            sum(len(i) for i in teens),
            # Add the tens:
            sum(len(i) for i in tens),

            # add the rest from 20 to 90
            8 * sum(len(i) for i in units),
            9 * sum(len(i) for i in tens[2:])])

        # a has all of the numbers counted from 1-99 inclusive
        # We need to count this 9 times
        # Then we add the number of numbers of hundreds
        ret += sum([
            # Add all the 1-99 for all numbers orders from 0-100,
            # 100-200, etc
            10 * a,
            # Add the extra words
            900 * (len('hundred')),
            # Subtract them for 100, 200, etc
            (900 - 9) * (len('and')),
            # Add the hundred orders
            100 * sum(len(i) for i in units)])

    else:
        raise NotImplementedError("TBD")

    return ret


def test_solution(limit):
    repl = re.compile('[\s,-]')

    return sum(len(repl.sub('', P.number_to_words(i)))
               for i in range(1, limit + 1))


def main():
    """The main function
    """
    print(benchmark(solution, 1000))
    print(benchmark(test_solution, 1000))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
