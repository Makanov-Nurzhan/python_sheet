
from collections import deque


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = deque([self])
        while queue:
            node = queue.popleft()
            array.append(node.name)
            for ch in node.children:
                queue.append(ch)
        return array


def isSymmetric(root):
    if not root:
        return True

    queue = deque([(root.left, root.right)])

    while queue:
        left, right = queue.popleft()

        if not left and not right:
            continue

        if not left or not right or left.val != right.val:
            return False

        queue.append((left.left, right.right))
        queue.append((left.right, right.left))

    return True
