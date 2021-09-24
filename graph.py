"""
>>> g = Graph({
...     'U': {'V': 2, 'W': 5, 'X': 1},
...     'V': {'U': 2, 'X': 2, 'W': 3},
...     'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
...     'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
...     'Y': {'X': 1, 'W': 1, 'Z': 1},
...     'Z': {'W': 5, 'Y': 1},
... })

>>> list(g.iter_breadth_first("U"))
['U', 'V', 'W', 'X', 'Y', 'Z']

>>> list(g.iter_breadth_first("V"))
['V', 'U', 'X', 'W', 'Y', 'Z']

>>> list(g.iter_breadth_first("Y"))
['Y', 'X', 'W', 'Z', 'U', 'V']

>>> list(g.iter_depth_first("Z"))
['Z', 'Y', 'W', 'X', 'V', 'U']

>>> list(g.iter_depth_first("U"))
['U', 'X', 'Y', 'Z', 'W', 'V']

>>> list(g.iter_depth_first_post("Z"))
['U', 'V', 'X', 'W', 'Y', 'Z']

>>> list(g.iter_depth_first_recursive("Z"))
['Z', 'Y', 'W', 'X', 'V', 'U']

>>> g.dijkstra("U")
({'U': 0, 'V': 2, 'W': 3, 'X': 1, 'Y': 2, 'Z': 3}, {'U': None, 'V': 'U', 'W': 'Y', 'X': 'U', 'Y': 'X', 'Z': 'Y'})

>>> g.dijkstra("X")
({'X': 0, 'U': 1, 'V': 2, 'W': 2, 'Y': 1, 'Z': 2}, {'X': None, 'U': 'X', 'V': 'X', 'W': 'Y', 'Y': 'X', 'Z': 'Y'})

>>> list(g.dijkstra_shortest_paths("U", "W"))
[('W', 3, ['U', 'X', 'Y', 'W']), ('W', 4, ['U', 'X', 'W']), ('W', 5, ['U', 'W'])]

"""

import collections
import heapq


class Graph(object):

    def __init__(self, verts):
        self.verts = collections.defaultdict(dict)
        self.verts.update(verts)

    def add_edge(self, from_: str, to: str, weight: int = 0):
        self.verts[from_][to] = weight

    def add_edge_bi(self, from_: str, to: str, weight: int = 0):
        self.verts[from_][to] = weight
        self.verts[to][from_] = weight

    def iter_breadth_first(self, start: str):
        # use a deque as a queue.
        q = collections.deque()
        seen = set()

        q.append(start)

        while q:
            v = q.popleft()

            if v not in seen:
                yield v
                seen.add(v)

            for (n, weight) in self.verts[v].items():
                if n in seen:
                    continue

                q.append(n)

    def iter_depth_first(self, start: str):
        # use a deque as a stack
        s = collections.deque([start])

        seen = set()

        while s:
            v = s.pop()

            if v not in seen:
                yield v
                seen.add(v)

            for (n, weight) in self.verts[v].items():
                if n in seen:
                    continue

                s.append(n)

    def iter_depth_first_post(self, start: str):
        s = collections.deque([start])
        post = collections.deque()

        seen = set()

        while s:
            v = s.pop()

            if v not in seen:
                post.append(v)
                seen.add(v)

            for (n, weight) in self.verts[v].items():
                if n in seen:
                    continue

                s.append(n)

        while post:
            v = post.pop()

            yield v

    def iter_depth_first_recursive(self, start: str, seen=set()):
        if start not in seen:
            seen.add(start)
            yield start

        for n in reversed(self.verts[start].keys()):
            if n in seen:
                continue

            yield from self.iter_depth_first_recursive(n, seen)



    def dijkstra(self, start: str):
        distances = collections.defaultdict(lambda: float("inf"))
        distances[start] = 0

        prev = {}
        prev[start] = None

        q = [(0, start)]

        while q:
            distance, v = heapq.heappop(q)

            if distance > distances[v]:
                continue

            for n, weight in self.verts[v].items():
                ndistance = distance + weight

                if ndistance >= distances[n]:
                    continue

                distances[n] = ndistance
                prev[n] = v
                heapq.heappush(q, (ndistance, n))

        return dict(distances), prev

    def dijkstra_shortest_paths(self, start: str, target: str):
        distances = collections.defaultdict(lambda: float("inf"))
        distances[start] = 0

        q = [(0, [start])]

        while q:
            distance, path = heapq.heappop(q)
            v = path[-1]

            if v == target:
                yield v, distance, path

            if distance > distances[v]:
                continue

            for n, weight in self.verts[v].items():
                ndistance = distance + weight

                if ndistance >= distances[n]:
                    continue

                distances[n] = ndistance
                heapq.heappush(q, (ndistance, path + [n]))
