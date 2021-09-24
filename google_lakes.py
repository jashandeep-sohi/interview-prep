"""
>>> capacity([1,3,2,4,1,3,1,4,5,2,2,1,4,2,2])
15
"""

import collections
import heapq
import typing as t

def capacity(heights: list[int]) -> int:
    g = collections.defaultdict(set)

    for i in range(1, len(heights)):
        g[str(i - 1)].add(str(i))
        g[str(i)].add(str(i - 1))

    g["0"].add("sink")
    g[str(len(heights) - 1)].add("sink")

    waterlevels = [waterlevel(x, g, heights) for x in range(len(heights))]
    volumes = [wl - h for wl, h in zip(waterlevels, heights)]

    return sum(volumes)


def waterlevel(x, g, heights) -> int:
    pq = [(heights[x], str(x))]
    seen = set()

    while pq:
        height, v = heapq.heappop(pq)

        if v == "sink":
            return height

        if v in seen:
            continue
        seen.add(v)

        for n in g[v]:
            if n in seen:
                continue
            if n == "sink":
                heapq.heappush(pq, (height, n))
            else:
                heapq.heappush(pq, (max(height, heights[int(n)]), n))
    return 0
