NAME = "Factorial"
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

    total = 1
    for value in data:
        steps.append({
            "type": "compare",
            "index": value,
            "array": data.copy(),
        })
        total *= value

    steps.append({
        "type": "finished",
        "array": [total],
    })

    return steps
