"""
>>> freq(["i","love","leetcode","i","love","coding"], 2)
['i', 'love']

>>> freq(["the","day","is","sunny","the","the","the","sunny","is","is"], 4)
['the', 'is', 'sunny', 'day']
"""

import collections
import heapq

def freq(words: list[str], k: int) -> list[str]:
    counts = collections.Counter(words) # O(n)
    heap = []

    for word, count in counts.items(): # O(n log k)
        if len(heap) < k:
            heapq.heappush(heap, (count, word))
        else:
            # push and return the smallest
            heapq.heappushpop(heap, (count, word))

    heap = [(-count, word) for count, word in heap] # O(k)
    heapq.heapify(heap) # O(k)
    result = []
    while heap: # O(k log k)
        result.append(heapq.heappop(heap)[1])

    return result
