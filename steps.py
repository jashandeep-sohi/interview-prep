"""
>>> steps(1) # 1
1
>>> steps(2) # 1 1, 2
2
>>> steps(3) # 1 1 1, 2 1, 1 2
3
>>> steps(4) # 1 1 1 1, 1 1 2, 2 1 1, 1 2 1, 2 2
5
>>> steps(5) # 1 1 1 1 1, 1 1 1 2, 1 1 2 1, 1 2 1 1, 2 1 1 1, 2 2 1, 1 2 2, 2 1 2
8
"""


def steps(n):
    if n == 0 or n == 1:
        return 1

    return steps(n - 1) + steps(n - 2)
