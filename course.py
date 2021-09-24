"""
>>> course(2, [[1,0]])
[0, 1]

>>> x = course(4, [[1,0], [2,0], [3,1], [3,2]])
>>> x == [0, 1, 2, 3] or x == [0, 2, 1, 3]
True

>>> course(1, [])
[0]

>>> course(4, [[1, 2], [2, 3], [3, 1], [0, 3]])
[]


"""

import collections


def course(ncourse: int, prereqs: list[list[int]]) -> list[int]:
    result = collections.deque()

    g = {}

    for i in range(ncourse):
        g[i] = set()

    for prereq in prereqs:
        course, req = prereq
        g[course].add(req)

    seen = set()
    for start in range(ncourse):
        # if df(g, start, seen, result, start):
        #     return []

        s = collections.deque([start])
        post = collections.deque()

        while s:
            v = s.pop()

            if v in seen:
                if v == start:
                    return []
                continue

            post.append(v)
            seen.add(v)

            for n in g[v]:
                s.append(n)

        while post:
            result.append(post.pop())

    return list(result)


def df(g, start, seen, result, og_start):
    if start in seen:
        if start == og_start:
            return True
        return False

    seen.add(start)

    for c in g[start]:
        if df(g, c, seen, result, og_start):
            return True

    result.append(start)
