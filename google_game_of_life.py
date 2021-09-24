"""
>>> game([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])
[[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]

>>> game([[1,1],[1,0]])
[[1, 1], [1, 1]]
"""

import collections

def game(board: list[list[int]]) -> list[list[int]]:
    b = collections.defaultdict(lambda: 0)

    cols = len(board[0])
    rows = len(board)

    for row in range(rows):
        for col in range(cols):
            b[(row, col)] = board[row][col]

    for row in range(rows):
        for col in range(cols):
            neighbors = (
                b[(row, col - 1)], # left
                b[(row - 1, col - 1)], # top-left
                b[(row - 1, col)], # top
                b[(row - 1, col + 1)], # top-right
                b[(row, col + 1)], # right
                b[(row + 1, col + 1)], # bottom-right
                b[(row + 1, col)], # botom
                b[(row + 1, col - 1)] # bottom-left
            )

            nsum = sum(neighbors)

            alive = b[(row, col)]

            if (not alive and nsum == 3) or (alive and nsum == 2 or nsum == 3):
                board[row][col] = 1
            else:
                board[row][col] = 0

    return board

