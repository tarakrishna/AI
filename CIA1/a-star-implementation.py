import heapq

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

def a_star(graph, start, goal, heuristics):
    queue = [(0 + heuristics[start], 0, start, [start])]
    visited = set()

    while queue:
        (f, g, node, path) = heapq.heappop(queue)
        
        if node == goal:
            return path, g
        
        if node in visited:
            continue
        
        visited.add(node)
        
        for neighbor, cost in graph[node].items():
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristics[neighbor]
                heapq.heappush(queue, (new_f, new_g, neighbor, path + [neighbor]))

    return None, None

# Example usage
print(a_star(graph, 'S', 'G', heuristics))
