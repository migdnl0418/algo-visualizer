NAME = "Binary Tree"
TYPE = "sort"


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def _insert(node, value):
            if node is None:
                return Node(value)

            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)

            return node

        self.root = _insert(self.root, value)
        return self.root

    def inorder(self):
        values = []

        def _walk(node):
            if node is None:
                return
            _walk(node.left)
            values.append(node.value)
            _walk(node.right)

        _walk(self.root)
        return values


def run(numbers):
    steps = []
    tree = BinarySearchTree()

    for value in numbers:
        tree.insert(value)
        steps.append({
            "type": "compare",
            "index": value,
            "array": tree.inorder(),
        })

    steps.append({
        "type": "finished",
        "array": sorted(numbers),
    })

    return steps
