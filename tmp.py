#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Question:

"""

def solution():
    """
    Solution to the problem.
    """
    return 1


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
