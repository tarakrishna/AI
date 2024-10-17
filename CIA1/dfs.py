# Graph structure
graph = {
    'S': {'A': 3, 'B': 5},
    'A': {'B': 4, 'D': 3},
    'B': {'C': 4},
    'C': {'E': 6},
    'D': {'G': 5},
    'E': {},
    'G': {}
}

# Heuristic values
heuristics = {
    'S': 10,
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 3,
    'E': 2,
    'G': 0
}


def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()

    while stack:
        (node, path) = stack.pop()
        if node not in visited:
            if node == goal:
                return path
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    return None

# Example usage
print(dfs(graph, 'S', 'G'))
