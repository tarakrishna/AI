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


def hill_climbing(graph, start, goal, heuristics):
    current = start
    path = [current]

    while current != goal:
        neighbors = graph[current]
        if not neighbors:
            return None
        
        # Choose the neighbor with the best heuristic value
        next_node = min(neighbors, key=lambda n: heuristics[n])
        
        if heuristics[next_node] >= heuristics[current]:
            # If no improvement, we're at a local maximum
            return path
        
        current = next_node
        path.append(current)

    return path

# Example usage
print(hill_climbing(graph, 'S', 'G', heuristics))
