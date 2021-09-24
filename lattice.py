"""
>>> num_paths(1, 1)
1
>>> num_paths(1, 2)
1
>>> num_paths(1, 3)
1
>>> num_paths(2, 1)
1
>>> num_paths(2, 2) # num_paths(2, 1) + num_paths(1, 2)
2
>>> num_paths(2, 3) # num_paths(2, 2) + num_paths(1, 3)
3
>>> num_paths(3, 3) # num_paths(3, 2) + num_paths(2, 3)
6
>>> num_paths_iter(3, 3)
6
>>> all(num_paths_iter(w, h) == num_paths(w, h) for w in range(1, 10) for h in range(1, 10))
True
"""

import functools

@functools.cache
def num_paths(w: int, h: int) -> int:
    if w == 1 or h == 1:
        return 1

    return num_paths(w, h - 1) + num_paths(w - 1, h)


def num_paths_iter(w: int, h: int) -> int:
    lattice = [[0] * (h + 1) for _ in range(0, w + 1)]

    # seed so that 1, 1 will be 1 after summing
    lattice[0][1] = 1

    for row in range(1, w + 1):
        for col in range(1, h + 1):
            lattice[row][col] = lattice[row - 1][col] + lattice[row][col - 1]

    return lattice[-1][-1]
