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

def branch_and_bound_greedy_exit(graph, start, goal, heuristics):
    queue = [(heuristics[start], 0, start, [start])]

    while queue:
        (h, cost, node, path) = heapq.heappop(queue)
        
        if node == goal:
            return path, cost  # Early exit on first solution found
        
        for neighbor, edge_cost in graph[node].items():
            if neighbor not in path:
                new_cost = cost + edge_cost
                new_h = heuristics[neighbor]
                new_path = path + [neighbor]
                heapq.heappush(queue, (new_h, new_cost, neighbor, new_path))

    return None, None

# Example usage
print(branch_and_bound_greedy_exit(graph, 'S', 'G', heuristics))
