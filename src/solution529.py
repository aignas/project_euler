#!/usr/bin/python3

"""Project Euler 529.
"""


from collections import deque


def friendly_numbers(start, end, limit=10):
    """Gives the next friendly number

    >>> list(friendly_numbers(1, 1))
    []

    >>> list(friendly_numbers(1, 2))
    []

    >>> list(friendly_numbers(1, 10))
    []

    >>> list(friendly_numbers(1, 29))
    [19, 28]

    >> list(friendly_numbers(1, 10**2))
    [19, 28, 37, 46, 55, 64, 73, 82, 91]

    Some pseudo code for this generator:

        while :

    """
    number = start
    while number < end:
        digits = deque(int(i) for i in str(number))
        buff = deque()
        sum_ = 0

        while digits and sum_ < limit:
            buff.append(digits.popleft())
            sum_ += buff[-1]

        if sum_ != limit:
            # We know, that the last digit (at least) needs to go up and
            # we skip the rest of the loop, however, if there are no
            # digits left, we will get into an infinite loop
            if digits:
                number += 10**len(digits)
            else:
                number += 1
            continue

        counter = 0
        while digits:
            digit = digits.popleft()
            if sum_ == limit:
                counter = 0

            if sum_ <= limit:
                buff.append(digit)
                sum_ += digit
                counter += 1

            while sum_ > limit:
                if counter and counter == len(buff):
                    number += 10**counter
                    continue
                else:
                    sum_ -= buff.popleft()

        if sum_ == limit:
            yield number
        else:
            number += 1


def is_friendly(number, limit=10, *, debug=0):
    """This checks whether the number is D-string friendly

    >>> is_friendly(919191)
    True

    >>> is_friendly(919191, debug=1)
    91
    19
    91
    19
    91
    True

    >>> is_friendly(3523014, debug=1)
    352
    523
    5230
    23014
    True

    >>> is_friendly(28546, debug=1)
    28
    False

    """
    digits = deque(int(i) for i in str(number))
    buff = deque()
    sum_ = 0

    while digits and sum_ < limit:
        buff.append(digits.popleft())
        sum_ += buff[-1]

    if sum_ != limit:
        return False

    if debug > 0:
        print(''.join(str(i) for i in buff))

    counter = 0
    for digit in digits:
        if sum_ == limit:
            counter = 0

        if sum_ <= limit:
            buff.append(digit)
            sum_ += digit
            counter += 1

        while sum_ > limit:
            if counter == len(buff):
                return False
            else:
                sum_ -= buff.popleft()

        if debug > 0 and sum_ == limit:
            print(''.join(str(i) for i in buff))

    return sum_ == limit


def total(order):
    """Returns the total number.

    >> [total(i) for i in range(6)]
    [0, 0, 9, 72, 507, 3492]

    """
    return sum(1 for i in friendly_numbers(1, 10**order))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
