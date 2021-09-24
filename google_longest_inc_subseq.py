"""
>>> longest_seq([10,9,2,5,3,7,101,18])
4
"""

import bisect

def longest_seq(nums: list[int]) -> int:
    s = []

    for n in nums: # O(n)
        i = bisect.bisect_left(s, n) # O(log n)

        if i == len(s):
            s.append(n)
        else:
            s[i] = n

    return len(s)
