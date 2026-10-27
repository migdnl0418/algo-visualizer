NAME = "Bubble Sort"
TYPE = "sort"


def run(numbers):
    steps = []
    data = numbers.copy()

    n = len(data)

    for i in range(n):
        for j in range(0, n - i - 1):
            steps.append({
                "type": "compare",
                "index1": j,
                "index2": j + 1,
                "array": data.copy()
            })

            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                steps.append({
                    "type": "swap",
                    "index1": j,
                    "index2": j + 1,
                    "array": data.copy()
                })

    steps.append({
        "type": "finished",
        "array": data.copy()
    })

    return steps
