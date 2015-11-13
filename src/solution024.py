
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Project Euler solution

    Problem 24: Lexicographic permutations



    A permutation is an ordered arrangement of objects. For example, 3124 is
    one possible permutation of the digits 1, 2, 3 and 4. If all of the
    permutations are listed numerically or alphabetically, we call it
    lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

    What is the millionth lexicographic permutation of the digits 0, 1, 2, 3,
    4, 5, 6, 7, 8 and 9?


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
