NAME = "Graph"
TYPE = "sort"

from collections import deque


def run(numbers):
    steps = []
    nodes = list(numbers)

    if not nodes:
        steps.append({
            "type": "finished",
            "array": [],
        })
        return steps

    graph = {node: [] for node in nodes}

    for index in range(len(nodes) - 1):
        current = nodes[index]
        next_node = nodes[index + 1]
        graph[current].append(next_node)
        graph[next_node].append(current)

    visited = set()
    queue = deque([nodes[0]])
    visited.add(nodes[0])

    while queue:
        current = queue.popleft()
        steps.append({
            "type": "compare",
            "index": nodes.index(current),
            "array": list(graph.keys()),
        })

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    steps.append({
        "type": "finished",
        "array": list(nodes),
    })

    return steps
