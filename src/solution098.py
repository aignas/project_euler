#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Project Euler 23.

Question:
    By replacing each of the letters in the word CARE with 1, 2, 9, and
    6 respectively, we form a square number: 1296 = 36**2. What is
    remarkable is that, by using the same digital substitutions, the
    anagram, RACE, also forms a square number: 9216 = 96**2. We shall call
    CARE (and RACE) a square anagram word pair and specify further that
    leading zeroes are not permitted, neither may a different letter
    have the same digital value as another letter.

    Using words.txt (right click and 'Save Link/Target As...'), a 16K
    text file containing nearly two-thousand common English words, find
    all the square anagram word pairs (a palindromic word is NOT
    considered to be an anagram of itself).

    What is the largest square number formed by any member of such a
    pair?

    NOTE: All anagrams formed must be contained in the given text file.
"""

from collections import defaultdict
from itertools import permutations
from itertools import combinations


def find_anagrams():
    """Factorial function

    >>> a = find_anagrams()
    >>> len(a)
    42
    >>> max(len(i) for i in a)
    3

    """
    anagram_sets = defaultdict(list)

    with open("problem098_words.txt", "r") as file_:
        # Generate a list of strings
        words = [i.replace("\"", "") for i in file_.read().split(',')]

    # Remove duplicates:
    words = list(set(words))

    # Traverse the list, so that we find all anagrams
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagram_sets[sorted_word].append(word)

    # Now, remove all the keys, that do not have any anagrams
    anagrams = [value for value in anagram_sets.values()
                if len(value) > 1]

    return sorted_by_length(anagrams)


def sorted_by_length(anagrams, reverse=True):
    """In order to find the largest, we need to start first with the
    longest anagram pairs.

    >>> sorted_by_length([("RACE", "RACE"), ("TWO", "TWO"), ("ILLUSION", "ILLUSION")])
    [('ILLUSION', 'ILLUSION'), ('RACE', 'RACE'), ('TWO', 'TWO')]

    """
    return sorted(anagrams, key=lambda x: len(x[0]), reverse=reverse)


def anagram_pairs():
    """This takes all of the anagrams and generates anagram pairs.

    >>> a = iter(anagram_pairs())

    """
    anagrams = find_anagrams()
    for anagram_set in sorted_by_length(anagrams):
        for comb in combinations(anagram_set, 2):
            yield comb


def get_max_square(first, second):
    """This checks if the anagram pair is the square pair.

    >>> a = get_max_square("RACE", "CARE")
    >>> a != 0
    True

    """
    assert len(first) == len(second)

    max_square = 0

    import string
    for perm in permutations(string.digits, len(first)):
        # We know that the first letters cannot be zeros, hence, we
        # should exclude these by just continuing:
        if perm[0] == '0' or perm[first.index(second[0])] == '0':
            continue

        first_number = int(''.join(perm))
        second_number = int(''.join(
            [perm[first.index(i)] for i in second]))

        if int(first_number**0.5)**2 == first_number and \
                int(second_number**0.5)**2 == second_number:
            max_square = max(first_number, second_number, max_square)

    return max_square


def main(benchmark=False):
    """Main loop

    Sum of the digits.

    """
    from timeit import default_timer as timer

    start = timer()
    answer = 0
    for one, other in anagram_pairs():
        answer = max(answer, get_max_square(one, other))
        if answer > 10**(len(one) + 1):
            break
    end = timer()
    if benchmark:
        print("Completed in: {}".format(end - start))
    return answer


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(main(True))
