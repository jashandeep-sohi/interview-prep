"""
>>> redundant([[1,2], [1,3], [2,3]])
[2, 3]

>>> redundant([[1,2],[2,3],[3,4],[1,4],[1,5],[5,6],[4,6]])
[1, 4]
"""

import collections

def dfs(g, start, stop):
    seen = {start}
    stack = collections.deque([start])

    while stack:
        v = stack.pop()

        if v == stop:
            return True

        for n in g[v]:
            if n in seen:
                continue
            stack.append(n)
            seen.add(v)

    return False

def redundant(edges: list[list[int]]) -> list[int]:
    g = collections.defaultdict(set)

    result = []

    for edge in edges:
        a, b = edge
        if a in g and b in g and dfs(g, a, b):
            result = edge
        g[a].add(b)
        g[b].add(a)

    return result
