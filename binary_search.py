"""
  >>> x = list(range(100))
  >>> all(binary_search(x, n) for n in x)
  True
  >>> binary_search(x, 100)
  False

  >>> all(binary_search_two(x, n) for n in x)
  True
  >>> binary_search_two(x, 100)
  False

  >>> x = list(range(100))
  >>> all(binary_search_iterative(x, n) for n in x)
  True
  >>> binary_search_iterative(x, 100)
  False
"""

def binary_search(nums: list[int], target: int) -> bool:
    return _binary_search(nums, target, 0, len(nums) - 1)

def _binary_search(nums: list[int], target: int, low: int, high: int) -> bool:
    if low > high:
        return False

    midpoint = low + (high - low) // 2

    if nums[midpoint] == target:
        return True
    elif target > nums[midpoint]:
        return _binary_search(nums, target, midpoint + 1, high)
    else:
        return _binary_search(nums, target, low, midpoint - 1)

def binary_search_two(nums: list[int], target: int) -> bool:
    if len(nums) <= 0:
        return False

    midpoint = len(nums) // 2

    if nums[midpoint] == target:
        return True
    if target < nums[midpoint]:
        return binary_search_two(nums[:midpoint], target)
    else:
        return binary_search_two(nums[midpoint+1:], target)


def binary_search_iterative(nums: list[int], target: int) -> bool:
    low = 0
    high = len(nums) - 1

    while low <= high:
        midpoint = low + (high - low) // 2

        if target == nums[midpoint]:
            return True
        elif target > nums[midpoint]:
            low = midpoint + 1
        else:
            high = midpoint - 1

    return False
