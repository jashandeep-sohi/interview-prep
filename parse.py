"""

"""

def evalf(s: str) -> int:
    tokens  = iter(s.split())

    stack = []

    for t in tokens:
        if t == "(":
            stack.append([])
        elif t in set("*+"):
            stack[-1].append(t)
        elif t == ")":
            func = stack.pop()
            func_name = func[0]
            func_args = func[1:]
        else:
            stack[-1].append(t)

