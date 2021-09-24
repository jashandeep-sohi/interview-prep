"""
>>> decompress("3[abc]4[ab]c")
'abcabcabcababababc'
>>> decompress("10[a]")
'aaaaaaaaaa'
>>> decompress("2[3[a]2[b]]")
'aaabbaaabb'
"""

import collections

def decompress(s: str) -> str:
    stack = collections.deque()

    for char in s:
        if char == "]":
            # process stack

            # first destack the string that needs to be repeated
            torepeat = collections.deque()
            while True:
                p = stack.pop()
                if p == "[":
                    break
                torepeat.appendleft(p)

            torepeat = "".join(torepeat)

            # destack the digits of number of times to repeat
            repeat = 0
            i = 0
            while stack:
                d = stack.pop()
                if not d.isdigit(): # to catch either [ or already decompressed letters
                    stack.append(d)
                    break
                repeat = repeat + int(d) * 10**i
                i = i + 1

            stack.append(repeat * torepeat)
        else:
            stack.append(char)

    return "".join(stack)
