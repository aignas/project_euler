
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


from math import factorial


def solution():
    """The solution to the problem

    The idea here is that the number of permutations is 10! and we need
    to go only through a subset of them in order to find the millionth
    one.

    There are 9! permutations with '0' in front. 9! is 362880.
    There are another 9! permutations with '1', which is another 362880,
    so our solution must have 2 in front.

    There are 8! with '20' in front and there are:
    40320

    NOTE: In order to get the correct answer, we need to subtract from our limit 1.

    """
    limit = 1000000 - 1
    digits = list('0123456789')
    number = ''

    solutions = factorial(len(digits))

    while len(number) < 10:
        solutions = solutions // len(digits)
        digit_to_choose = limit // solutions
        limit = limit % solutions
        number = number + digits[digit_to_choose]
        digits.pop(digit_to_choose)

    return int(number)


def main():
    """The main function
    """
    print(benchmark(solution))


if __name__ == "__main__":
    import doctest
    if doctest.testmod()[0] == 0:
        main()
