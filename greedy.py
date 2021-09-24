"""
>>> make_change(18, {5, 2, 1})
(True, [5, 5, 5, 2, 1])
"""

import heapq

def make_change(target: int, coins: set[int]) -> tuple[bool, list[int]]:
    result: list[int] = []

    coin_heap = [-x for x in coins]
    heapq.heapify(coin_heap)

    while coin_heap:
        coin = -heapq.heappop(coin_heap)

        q, r = divmod(target, coin)

        result.extend([coin] * q)

        target = r

    return not target, result
