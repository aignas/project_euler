#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Project Euler solution

    Problem 22: Names scores



    Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
    containing over five-thousand first names, begin by sorting it into
    alphabetical order. Then working out the alphabetical value for each name,
    multiply this value by its alphabetical position in the list to obtain a
    name score.

    For example, when the list is sorted into alphabetical order, COLIN, which
    is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
    COLIN would obtain a score of 938 × 53 = 49714.

    What is the total of all the name scores in the file?


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


import string


def solution():
    """The solution to the problem
    """
    with open("problem022.txt", 'r') as file_:
        # Sort the names straight away:
        names = sorted(file_.read().replace('"', '').replace(',', ' ').split())
        letters = string.ascii_uppercase
        translation_dict = {k: v for v, k in enumerate(letters, start=1)}
        return sum(
            i * sum(translation_dict[l] for l in s)
            for i, s in enumerate(names, start=1))


def main():
    """The main function
    """
    print(benchmark(solution))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
