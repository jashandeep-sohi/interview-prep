"""
>>> convert("A + B * C")
'A B C * +'
>>> convert("A * B + C")
'A B * C +'
>>> convert("A + B")
'A B +'
>>> convert("A * B")
'A B *'
>>> convert("( A * B )")
'A B *'
>>> convert("( A + B ) * C")
'A B + C *'
>>> convert("C * ( A + B )")
'C A B + *'
>>> convert("C * A + B")
'C A * B +'
>>> convert("A * B + C * D")
'A B * C D * +'
>>> convert("( A + B ) * C - ( D - E ) * ( F + G )")
'A B + C * D E - F G + * -'
>>> convert("( A + B ) * ( C + D )")
'A B + C D + *'
>>> convert("( A + B ) * C")
'A B + C *'
>>> convert("A + B * C")
'A B C * +'
"""

import collections


def convert(s: str) -> str:
    out = collections.deque()

    ops = {
        "*": 1,
        "-": 0,
        "+": 0,
        "/": 1,
        "(": -1,
    }

    op_stack = collections.deque()

    for t in s.split():
        if t == "(":
            op_stack.append(t)
        elif t == ")":
            out.append(op_stack.pop())
            op_stack.pop()
        elif t in ops:
            if op_stack and ops[t] < ops[op_stack[-1]]:
                out.append(op_stack.pop())
                op_stack.append(t)
            else:
                op_stack.append(t)
        else:
            out.append(t)

    while op_stack:
        out.append(op_stack.pop())

    return " ".join(out)
