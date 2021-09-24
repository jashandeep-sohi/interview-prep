"""
>>> import random
>>> x = [98, 57, 26, 30, 7, 84, 16, 55, 20, 71]
>>> y = random.sample(range(0, 1000), random.randint(0, 100))


>>> heapsort(x)
[7, 16, 20, 26, 30, 55, 57, 71, 84, 98]


>>> mergesort(x)
[7, 16, 20, 26, 30, 55, 57, 71, 84, 98]
>>> assert mergesort(y) == sorted(y)
>>> assert mergesort_iter(y) == sorted(y)


>>> quicksort(x)
[7, 16, 20, 26, 30, 55, 57, 71, 84, 98]
>>> assert quicksort(y) == sorted(y)


>>> insertionsort(x)
[7, 16, 20, 26, 30, 55, 57, 71, 84, 98]
>>> assert insertionsort(y) == sorted(y)


>>> bubblesort(x)
[7, 16, 20, 26, 30, 55, 57, 71, 84, 98]
>>> assert bubblesort(y) == sorted(y)
>>> bubblesort([])
[]
>>> bubblesort([1, 1])
[1, 1]


>>> selectionsort(x)
[7, 16, 20, 26, 30, 55, 57, 71, 84, 98]
>>> assert selectionsort(y) == sorted(y)
>>> selectionsort([])
[]
>>> selectionsort([1, 1])
[1, 1]
>>> selectionsort([1])
[1]


>>> shellsort(x)
[7, 16, 20, 26, 30, 55, 57, 71, 84, 98]
>>> assert shellsort(y) == sorted(y)


>>> bucketsort(x, 10)
[7, 16, 20, 26, 30, 55, 57, 71, 84, 98]
>>> assert bucketsort(y, random.randint(1, 10)) == sorted(y)
>>> bucketsort([], 1)
[]


>>> radixsort(x)
[7, 16, 20, 26, 30, 55, 57, 71, 84, 98]
>>> assert radixsort(y) == sorted(y)


>>> countingsort(x)
[7, 16, 20, 26, 30, 55, 57, 71, 84, 98]
>>> assert countingsort(y) == sorted(y)
"""

import heapq
import random
import itertools
import typing as t
import collections


def countingsort(x: list[int]) -> list[int]:
    m = max(x)

    out = [0] * len(x)
    counts = [0] * (m + 1)

    for n in x:
        counts[n] = counts[n] + 1

    for i in range(1, len(counts)):
        counts[i] = counts[i] + counts[i - 1]

    for i in reversed(range(0, len(x))):
        n = x[i]
        out_index = counts[n] - 1
        out[out_index] = n
        counts[n] = counts[n] - 1

    return out


def radixsort(x: list[int]) -> list[int]:
    if not len(x) > 0:
        return x

    m = max(x)
    passes = len(str(m))

    for p in range(passes):
        x = _radixsort(x, p)

    return x


def _radixsort(x: list[int], p: int) -> list[int]:
    buckets = [[] for _ in range(10)]

    for n in x:
        bucket_index = (n // (10 ** p)) % 10

        buckets[bucket_index].append(n)

    return list(itertools.chain(*buckets))


def bucketsort(x: list[int], k: int) -> list[int]:
    if not len(x) > 0:
        return x

    if not k >= 1:
        raise ValueError("k must be >= 1")

    buckets = [[] for _ in range(k)]
    m = max(x)

    for n in x:
        bucket_index = int((k - 1) * n // m)
        buckets[bucket_index].append(n)

    for bucket in buckets:
        _insertionsort(bucket)

    return list(itertools.chain(*buckets))


def shellsort(
    x: list[int],
    gaps: t.Iterable[int]=(
        701, 301, 132, 57, 23, 10, 4, 1
    )
) -> list[int]:
    x = list(x)

    for gap in gaps:
        for i in range(gap, len(x)):
            n = x[i]
            j = i
            while j >= gap and x[j - gap] > n:
                x[j] = x[j - gap]
                j = j - gap
            x[j] = n

    return x


def selectionsort(x: list[int]) -> list[int]:
    x = list(x)

    for i in range(len(x)):

        min_index = i
        for j in range(i, len(x)):
            if x[j] < x[min_index]:
                min_index = j

        x[i], x[min_index] = x[min_index], x[i]

    return x


def bubblesort(x: list[int]) -> list[int]:
    x = list(x)

    finished = False
    while not finished:
        finished = True
        for i in range(1, len(x)):
            if x[i - 1] > x[i]:
                x[i], x[i - 1] = x[i - 1], x[i]
                finished = False

    return x


def insertionsort(x: list[int]) -> list[int]:
    x = list(x)
    _insertionsort(x)
    return x


def _insertionsort(x: list[int]) -> None:
    for i in range(1, len(x)):
        n = x[i]
        j = i
        while j >= 1 and x[j - 1] > n:
            x[j] = x[j - 1]
            j = j - 1
        x[j] = n


def quicksort(x: list[int]) -> list[int]:
    return _quicksort(x)


def _quicksort(x) -> list[int]:
    if len(x) <= 1:
        return x

    pivot = x[random.randint(0, len(x) - 1)]

    less = []
    more = []
    equal = []

    for n in x:
        if n < pivot:
            less.append(n)
        elif n == pivot:
            equal.append(n)
        else:
            more.append(n)

    return _quicksort(less) + equal + _quicksort(more)


def heapsort(x: list[int]) -> list[int]:
    h = list(x)
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(h))]

def heapsortany(x: list[t.Any]) -> list[t.Any]:
    h = list(x)
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(h))]

def mergesort(x: list[int]) -> list[int]:
    x = list(x)
    _mergesort(x)
    return x


def mergesort_iter(x: list[int]) -> list[int]:
    return list(_mergesort_gen(x, 0, len(x)))


def _mergesort(x: list[int]) -> None:
    length = len(x)

    if length <= 1:
        return

    midpoint = length // 2

    left = x[:midpoint]
    right = x[midpoint:]

    _mergesort(left)
    _mergesort(right)

    left_index = right_index = x_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            x[x_index] = left[left_index]
            left_index += 1
        else:
            x[x_index] = right[right_index]
            right_index += 1

        x_index += 1

    if left_index < len(left):
        x[x_index:] = left[left_index:]

    if right_index < len(right):
        x[x_index:] = right[right_index:]



def _mergesort_gen(x: list[int], start: int, stop: int) -> t.Generator[int, None, None]:
    length = stop - start

    if length <= 1:
        yield from itertools.islice(x, start, stop)
        return

    midpoint = start + (length // 2)

    left_iter = _mergesort_gen(x, start, midpoint)
    right_iter = _mergesort_gen(x, midpoint, stop)

    left, right = next(left_iter, None), next(right_iter, None)

    while left is not None and right is not None:
        if left < right:
            yield left
            left = next(left_iter, None)
        else:
            yield right
            right = next(right_iter, None)

    if left is not None:
        yield left
        yield from left_iter

    if right is not None:
        yield right
        yield from right_iter

if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
