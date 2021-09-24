"""
>>> eval_s(a)
15
>>> eval_tree(a)
15
>>> eval_s(b)
15
>>> eval_tree(b)
15
>>> eval_s(c)
50
>>> eval_s(d)
15
>>> eval_s(e)
15
>>> eval_tree(e)
15
"""

a = "15"
b = "( + 5 10 )"
c = "( * 5 10 )"
d = "( + ( + 2 3 ) ( + 5 5 ) )"
e = "( + ( + ( + ( * 1 1 1 1 ) 1 ) 3 ) ( + 5 5 ) )"


import collections
import functools
import pprint


def eval_s(s: str) -> int:
    stack = collections.deque()
    stack.append({"op": None, "args": []})

    for t in s.split():
        if t == "(":
            # start of function
            stack.append({"op": None, "args": []})
        elif t in set("*+"):
            # op
            stack[-1]["op"] = t
        elif t == ")":
            # end of function
            f = stack.pop()
            if f["op"] == "+":
                res = sum(f["args"])
            else:
                res = functools.reduce(lambda a, b: a * b, f["args"])
            stack[-1]["args"].append(res)
        else:
            stack[-1]["args"].append(int(t))

    return stack.pop()["args"][0]


def eval_tree(s: str) -> int:
    root = {"value": "root", "children": []}

    stack = collections.deque()

    node = root
    for t in s.split():
        if t == "(":
            fnode = {"value": None, "children": []}
            node["children"].append(fnode)
            stack.append(node)
            node = fnode
        elif t in set("+*"):
            node["value"] = t
        elif t == ")":
            node = stack.pop()
        else:
            node["children"].append({"value": int(t), "children": []})

    evaluate(root["children"][0])

    return root["children"][0]["value"]

def evaluate(node):
    op = node["value"]
    if op not in set("*+"):
        return

    for c in node["children"]:
        evaluate(c)

    vals = [c["value"] for c in node["children"]]

    if op == "*":
        res = functools.reduce(lambda a, b: a * b, vals)
    else:
        res = sum(vals)

    node["value"] = res
    node["children"] = []

