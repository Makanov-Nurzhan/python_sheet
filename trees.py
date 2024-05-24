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
