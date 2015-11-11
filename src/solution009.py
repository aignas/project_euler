#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def main():
    '''
    a + b + c = 1000
    a^2 + b^2 = c^2 = (1000 - b - a)^2 = 1000000 + b^2 + a ^2 - 2000b - 2000a + 2ab
    0 = 1e6 - 2000(a + b) + 2ab
    1000(a + b) -  ab = 5e5

    # The parametric equation is:
    a + b - 0.001 * ab = 500
    b (1 - 0.001 a) = 500 - a
    b = (500 - a)/(1- 0.001a)

    # The other equation is that int(b) == b

    The largest possible a can be found approximately as follows:
    a < b < c
    332 < 333 < 335
    '''
    for a in range(1, 334):
        b = (500 - a)/(1-0.001*a)
        if int(b) == b:
            break

    c = 1000 - a - b

    print(a,b,c)
    print(a*b*c)

if __name__ == "__main__":
    main()
