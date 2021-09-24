"""
>>> is_squre(["BALL", "AREA", "LEAD", "LADY"])
True
>>> find_square(["AREA", "BALL", "DEAR", "LADY", "LEAD", "YARD"])

100B = 100 * 10^9 = 10^11
1K = 10^6

n!/(n-r)!
10^11 ! / (10^8)! = 1 * 2 * 3 ... 10^11 / 1 * 2 * 3 ... 10^8 = (10^8 + 1) * (10^8 + 2) ... 10^11 = 10^11 ... 10^8 + 1 = kj 
  """

import collections
import itertools


def is_sqaure(words: tuple[str]) -> bool:
    for i, word in enumerate(words):
        for j, c in enumerate(word):
            if c != words[j][i]:
                return False

    return True


def find_square(words: list[str]) -> list[tuple[str]]:
    words_by_length = collections.defaultdict(set)

    for w in words:
        words_by_length[len(w)].add(w)

    res = []

    for length, words in words_by_length.items():
        for permutation in itertools.permutations(words, length):
            if is_sqaure(permutation):
                res.append(permutation)

    return res
