"""
>>> four_sum([1, 0, -1, 0, -2, 2], 0)
[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

>>> four_sum([2,2,2,2,2], 8)
[[2,2,2,2]]

>>> two_sum([1, 1, 2, 0, 1, 1, 2], 2)
[(1, 1), (0, 2)]
"""


def four_sum(nums: list[int], target: int) -> list[tuple[int]]:
    return kth_sum(4, nums, target)


def two_sum(nums: list[int], target: int) -> list[tuple[int]]:
    result = list()
    seen = set()

    for n in nums:
        need = target - n

        if need in seen:
            result.append((n, need))

        seen.add(n)

    return result


def kth_sum(k: int, nums: list[int], target: int) -> list[tuple[int]]:
    if k == 2:
        return two_sum(nums, target)

    result = []
    for i, n in enumerate(nums):
        need = target - n
        new_nums = nums[:i] + nums[i+1:]

        for prev_sum in kth_sum(k - 1, nums[:i] + nums[i+1:], need):
            result.append((n,) + prev_sum)

    return result
