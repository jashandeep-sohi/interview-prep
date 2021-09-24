"""
>>> x = [5, 19, 1, 2, 22, 3]

>>> smallest_index(x)
2

>>> smallest(x)
1

>>> second_smallest(x)
2

>>> nth_smallest(x, 1)
1

>>> nth_smallest(x, 2)
2

>>> nth_smallest(x, 3)
3

>>> nth_smallest(x, 4)
5

>>> nth_smallest(x, 5)
19

>>> nth_smallest_faster(x, 1)
1

>>> nth_smallest_faster(x, 2)
2

>>> nth_smallest_faster(x, 3)
3

>>> nth_smallest_faster(x, 4)
5

>>> nth_smallest_faster(x, 5)
19

>>> nth_smallest_faster(x, 6)
23
"""

def smallest_index(nums: list[int]) -> int:
    index = 0
    for i, n in enumerate(nums[1:], 1):
        if n < nums[index]:
            index = i
    return index

def smallest(nums: list[int]) -> int:
    return nums[smallest_index(nums)]

def second_smallest(nums: list[int]) -> int:
    first_index = smallest_index(nums)

    return smallest(nums[:first_index] + nums[first_index + 1:])

def nth_smallest(nums: list[int], n: int) -> int:
    for _ in range(n - 1):
        prev_index = smallest_index(nums)
        nums = nums[:prev_index] + nums[prev_index + 1:]

    return smallest(nums)

def nth_smallest_faster(nums: list[int], n: int) -> int:
    first = nums[0]
    left = []
    right = []
    for num in nums[1:]:
        if num > first:
            right.append(num)
        else:
            left.append(num)

    first_n = len(left) + 1

    if first_n == n:
        return first
    elif n > first_n:
        return nth_smallest_faster(right, n - first_n)
    else:
        return nth_smallest_faster(left, n)


