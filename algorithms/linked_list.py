NAME = "Linked List"
TYPE = "sort"


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None

        if values is not None:
            for value in values:
                self.append(value)

    def append(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = node
            return node

        self.tail.next = node
        self.tail = node
        return node

    def to_list(self):
        values = []
        current = self.head

        while current is not None:
            values.append(current.value)
            current = current.next

        return values

    def __len__(self):
        return len(self.to_list())

    def __repr__(self):
        return repr(self.to_list())


def run(numbers):
    steps = []
    linked_list = LinkedList()

    for value in numbers:
        linked_list.append(value)
        steps.append({
            "type": "compare",
            "index": len(linked_list.to_list()) - 1,
            "array": linked_list.to_list(),
        })

    current = linked_list.head
    while current is not None:
        steps.append({
            "type": "swap",
            "index1": 0,
            "index2": 0,
            "array": linked_list.to_list(),
        })
        current = current.next

    steps.append({
        "type": "finished",
        "array": list(numbers),
    })

    return steps
