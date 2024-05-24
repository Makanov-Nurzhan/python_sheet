from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(node, value):
    # If the tree is empty, return a new node
    if node is None:
        return Node(value)

    # Otherwise, recur down the tree
    if value < node.value:
        node.left = insert(node.left, value)
    elif value > node.key:
        node.right = insert(node.right, value)
    # Return the (unchanged) node pointer
    return node


def findClosestValueInBst(tree, target):
    closest = tree.value
    while tree is not None:
        if abs(tree.value - target) < abs(closest - target):
            closest = tree.value
        if closest == target:
            break
        if tree.value > target:
            tree = tree.left
        else:
            tree = tree.right

    return closest


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# recursive dfs


def invertBinaryTree(tree):
    if tree is None:
        return
    tree.left, tree.right = tree.right, tree.left

    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)
    return tree

# iterable bfs


def invertBinaryTree(tree):
    queue = deque([tree])
    if tree is None:
        return
    while queue:
        node = queue.popleft()
        node.left, node.right = node.right, node.left

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return tree
