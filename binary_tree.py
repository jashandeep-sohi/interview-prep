"""
>>> tree = Node(1, left=Node(2, left=Node(4), right=Node(5)), right=Node(3))
>>> list(tree.iter_depth_first_inorder())
[4, 2, 5, 1, 3]
>>> list(tree.iter_depth_first_preorder())
[1, 2, 4, 5, 3]
>>> list(tree.iter_depth_first_postorder())
[4, 5, 2, 3, 1]
>>> list(tree.iter_depth_first_inorder_iterative())
[4, 2, 5, 1, 3]
>>> list(tree.iter_depth_first_preorder_iterative())
[1, 2, 4, 5, 3]
>>> list(tree.iter_depth_first_postorder_iterative())
[4, 5, 2, 3, 1]
>>> list(tree.iter_depth_first_postorder_iterative_two_stacks())
[4, 5, 2, 3, 1]
>>> list(tree.iter_breadth_first())
[1, 2, 3, 4, 5]
"""
from __future__ import annotations

import typing as t
from collections import deque

import dataclasses


@dataclasses.dataclass()
class Node:
    value: t.Any
    left: t.Optional[Node] = None
    right: t.Optional[Node] = None

    def __repr__(self):
        return f"{self.value}"


    def iter_depth_first_inorder(self) -> t.Generator[Node, None, None]:
        if self.left is not None:
            yield from self.left.iter_depth_first_inorder()

        yield self

        if self.right is not None:
            yield from self.right.iter_depth_first_inorder()

    def iter_depth_first_preorder(self) -> t.Generator[Node, None, None]:
        yield self

        if self.left is not None:
            yield from self.left.iter_depth_first_preorder()

        if self.right is not None:
            yield from self.right.iter_depth_first_preorder()

    def iter_depth_first_postorder(self) -> t.Generator[Node, None, None]:

        if self.left is not None:
            yield from self.left.iter_depth_first_postorder()

        if self.right is not None:
            yield from self.right.iter_depth_first_postorder()

        yield self

    def iter_depth_first_inorder_iterative(self) -> t.Generator[Node, None, None]:
        # use a deque as a stack
        q: deque[Node] = deque()

        n = self
        while True:
            if n is not None:
                q.append(n)
                n = n.left
            elif q:
                n = q.pop()
                yield n
                n = n.right
            else:
                break


    def iter_depth_first_preorder_iterative(self) -> t.Generator[Node, None, None]:
        # use deque as a stack
        q = deque([self])

        while q:
            n = q.pop()

            yield n

            if n.right is not None:
                q.append(n.right)

            if n.left is not None:
                q.append(n.left)

    def iter_depth_first_postorder_iterative(self) -> t.Generator[Node, None, None]:
        s: deque[Node] = deque()

        n = self
        while True:
            if n is not None:
                if n.right is not None:
                    s.append(n.right)
                s.append(n)

                n = n.left
            elif s:
                n = s.pop()
                if n.right is not None and s and n.right == s[-1]:
                    right = s.pop()
                    s.append(n)
                    n = right
                else:
                    yield n
                    n = None
            else:
                break

    def iter_depth_first_postorder_iterative_two_stacks(self) -> t.Generator[Node, None, None]:
        s: deque[Node] = deque([self])
        p: deque[Node] = deque()

        while s:
            n = s.pop()
            p.append(n)

            if n.left is not None:
                s.append(n.left)

            if n.right is not None:
                s.append(n.right)


        while p:
            n = p.pop()
            yield n


    def iter_breadth_first(self) -> t.Generator[Node, None, None]:
        # use a deque as a queue
        q = deque([self])

        while q:
            n = q.popleft()

            yield n

            if n.left is not None:
                q.append(n.left)

            if n.right is not None:
                q.append(n.right)

    def is_binary_tree(self) -> bool:
        if self.left is not None:
            for n in self.left.iter_depth_first_preorder():
                if not n.value < self.value:
                    return False

        if self.right is not None:
            for n in self.right.iter_depth_first_preorder():
                if not n.value > self.value:
                    return False

        return True

