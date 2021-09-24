"""
>>> fully_parenth("a + b")
"(a + b)"
>>> fully_parenth("a")
"a"
>>> fully_parenth("a + b * c")
"(a + (b * c))"
>>> fully_parenth("a * b + c")
"((a * b) + c)"
"""

from collections import deque


def fully_parenth(s: str) -> str:
    idents = deque()
    ops = deque()

    for c in s:
        if c == " ":
            continue

        if c in {"*", "+"}:
            c

    return s
