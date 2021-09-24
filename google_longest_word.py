"""
>>> longest_graph("abppeoplee", words={"able", "ale", "apple", "bale", "kangaroo", "people"})
'people'
"""


import collections
import typing as t
import pprint

class Trie:

    def __init__(self, value=None):
        self.value = value
        self.word = False
        self.children = collections.defaultdict(Trie)

    def add(self, word):
        node = self
        for c in word:
            node = node.children[c]
        node.word = True
        node.value = word


def longest_trie(s: str, words: list[str]) -> t.Optional[str]:
    t = Trie()

    for w in words:
        t.add(w)

    tries = {t}
    for c in s:
        new_tries = set()
        for t in tries:
            new_tries.add(t)
            if c in t.children:
                new_tries.add(t.children[c])

        tries = new_tries


    best = None
    for t in tries:
        if not t.word:
            continue

        if best is None or len(best) < len(t.value):
            best = t.value

    return best

def longest(s: str, words: list[str]) -> t.Optional[str]:
    g = collections.defaultdict(list)

    for word in words:
        t = (word, 0)
        g[t[0][t[1]]].append(t)

    found = []
    for c in s:
        for t in g[c]:
            t = (t[0], t[1] + 1)
            if t[1] == len(t[0]):
                found.append(t[0])
                continue

            g[t[0][t[1]]].append(t)

    longest_match = None
    for f in found:
        if longest_match is None or len(f) > len(longest_match):
            longest_match = f

    return longest_match


def longest_graph(s: str, words: list[str]) -> t.Optional[str]:
    g = collections.defaultdict(dict)

    # for i in range(len(s)):
    #     g["start"][i] = s[i]
    #     for j in range(i + 1, len(s)):
    #         g[i][j] = s[j]

    prev = None
    prev_s = set()
    for i in reversed(range(len(s))):
        g["start"][i] = {s[i]}
        if prev is None:
            prev = frozenset({i})
            prev_s = {s[i]}
            continue

        new_prev = frozenset(prev | {i})

        g[i][prev] = prev_s
        g[new_prev][i] = {s[i]}
        g[new_prev][prev] = prev_s

        prev = new_prev
        prev_s = {s[i]} | prev_s

    longest_match = None

    for word in words:
        stack = collections.deque()
        stack.append(("start", 0, ""))
        while stack:
            v, i, chars = stack.pop()

            if chars == word:
                if longest_match is None or len(word) > len(longest_match):
                    longest_match = word
                break

            for n, w in g[v].items():
                if not i < len(word) or word[i] not in w:
                    continue

                if len(w) == 1:
                    stack.append((n, i + 1, chars + word[i]))
                else:
                    stack.append((n, i, chars))

    return longest_match

