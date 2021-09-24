"""
>>> is_valid("()")
True
>>> is_valid("()[]{}")
True
>>> is_valid("(]")
False
>>> is_valid("([)]")
False
>>> is_valid("{[]}")
True
"""

from collections import deque

def is_valid(s: str) -> bool:
    stack = deque()

    brackets = {
      "(": ")",
      "[": "]",
      "{": "}",
    }

    for char in s:
        if char in brackets:
            # char is an open bracket
            stack.append(char)
        else:
            # char is a closed bracket
            try:
                b = stack.pop()
            except:
                # not balanced, too many closing brackets
                return False

            if brackets[b] != char:
                # not the correct type of closing bracket
                return False

    # if anything is left over, not balanced -- not enough closing brackets
    return len(stack) == 0
