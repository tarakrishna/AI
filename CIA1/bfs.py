from collections import deque

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

def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        (node, path) = queue.popleft()
        if node not in visited:
            if node == goal:
                return path
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return None

# Example usage
print(bfs(graph, 'S', 'G'))
