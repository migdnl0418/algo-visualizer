NAME = "Fibonacci"
TYPE = "sort"


def run(numbers):
    steps = []
    data = list(numbers) if isinstance(numbers, (list, tuple)) else [numbers]

    if not data:
        steps.append({
            "type": "finished",
            "array": [],
        })
        return steps

    target = data[0]
    prev, current = 0, 1
    sequence = []

    for _ in range(target):
        sequence.append(prev)
        steps.append({
            "type": "compare",
            "index": len(sequence) - 1,
            "array": sequence.copy(),
        })
        prev, current = current, prev + current

    steps.append({
        "type": "finished",
        "array": sequence.copy(),
    })

    return steps
