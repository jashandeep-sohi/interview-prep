"""
>>> to_binary(0)
'0'
>>> to_binary(1)
'1'
>>> to_binary(2)
'10'
>>> to_binary(3)
'11'
>>> to_base(3, 2)
'11'
>>> to_base(3, 10)
'3'
>>> to_base(3, 16)
'3'
>>> to_base(3, 3)
'10'
>>> to_base_recursive(3, 2)
'11'
>>> to_base_recursive(0, 2)
'0'
"""

import collections


def to_binary(num: int) -> str:
    d = collections.deque()

    while True:
        num, r = divmod(num, 2)
        d.appendleft(r)

        if num == 0:
            break

    return "".join(map(str, d))


def to_base(num: int, base: int) -> str:
    d = collections.deque()

    digits = "0123456789abcdef"

    while True:
        num, r = divmod(num, base)
        d.appendleft(r)

        if num == 0:
            break

    return "".join(digits[x] for x in d)


def to_base_recursive(num: int, base: int) -> str:
    digits = "0123456789abcdef"
    if num < base:
        return digits[num]

    q, r = divmod(num, base)

    return to_base_recursive(q, base) + digits[r]
