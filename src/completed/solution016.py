#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Project Euler 23.

Question:
    2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

    What is the sum of the digits of the number 2**1000?
"""


def main(args, benchmark=False):
    """Main loop

    Sum of the digits.

    >>> main(15)
    26

    """
    from timeit import default_timer as timer

    start = timer()
    answer = sum(int(i) for i in str(2**args))
    end = timer()
    if benchmark:
        print("Completed in: {}".format(end - start))
    return answer


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(main(1000, True))
