#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_multiples(n, limit=1000):
    if n > limit:
        return []

    r = [n]
    while True:
        r.append((len(r) + 1) * n)
        if r[-1] >= limit:
            r.pop()
            return r

three_m = get_multiples(3, 1000)
five_m = get_multiples(5, 1000)
comp = three_m + [i for i in five_m if i not in three_m]
print(sum(comp))
