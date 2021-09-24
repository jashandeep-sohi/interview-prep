"""
>>> evalp("4 5 6 * +")
34
>>> evalp("7 8 + 3 2 + /")
3
"""

import collections

def evalp(s: str) -> int:

    d = collections.deque()

    ops = {
        "*": lambda a, b: a * b,
        "/": lambda a, b: a // b,
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
    }

    for t in s.split():
        if t in ops:
            b, a = d.pop(), d.pop()
            d.append(ops[t](a, b))
        else:
            d.append(int(t))

    return d.pop()
