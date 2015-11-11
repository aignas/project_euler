#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Question:

    The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.

"""

def colatz_len(n):
    length = 0
    while n != 1:
        length += 1
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + 1

    return length

def solution():
    """
    Solution to the problem.
    """
    colatz_length = [1]
    for i in range(2, 10**6):
        n = i
        length = 0
        while n != 1:
            # Since we know the chain length for every number smaller
            # than i, we can just cache the lengths of the Colatz chains
            # and use them when we need to find the length of the chain
            # of n < i
            #
            # This speeds up the code substantially!  Execution time
            # dropped from 31.2s to 1.92s!
            if n < i:
                length += colatz_length[n - 1]
                break

            length += 1
            if n % 2 == 0:
                n //= 2
            else:
                n = 3*n + 1

        colatz_length.append(length)

    max_val = max(colatz_length)
    number = colatz_length.index(max_val) + 1
    print("{}: {}".format(number, max_val))
    return number


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
