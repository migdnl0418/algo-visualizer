NAME = "Hash Table"
TYPE = "sort"


class HashTable:
    def __init__(self, size=8):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key, value):
        bucket = self.table[self._hash(key)]

        for index, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[index] = (key, value)
                return value

        bucket.append((key, value))
        return value

    def get(self, key):
        bucket = self.table[self._hash(key)]

        for existing_key, value in bucket:
            if existing_key == key:
                return value

        raise KeyError(key)

    def items(self):
        values = []
        for bucket in self.table:
            for _, value in bucket:
                values.append(value)
        return values


def run(numbers):
    steps = []
    table = HashTable()

    for key, value in enumerate(numbers):
        table.put(key, value)
        bucket = table.table[table._hash(key)]
        steps.append({
            "type": "compare",
            "index": len(bucket) - 1,
            "array": table.items(),
        })

    steps.append({
        "type": "finished",
        "array": list(numbers),
    })

    return steps
