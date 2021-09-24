"""
>>> make_change(11, [1,2,5])
3
>>> make_change(3, [2])
-1
>>> make_change(0, [1])
0
>>> make_change(1, [1])
1
>>> make_change(2, [1])
2
"""

import collections


def make_change(amount: int, coins: list[int]) -> int:
    if amount == 0:
        return 0

    coins_deque = collections.deque(sorted(coins))

    change = []

    while coins_deque:
        coin = coins_deque.pop()
        q, amount = divmod(amount, coin)

        if q:
            change.extend([coin] * q)

    return -1 if not change or amount > 0 else len(change)
