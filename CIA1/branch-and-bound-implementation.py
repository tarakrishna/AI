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

def branch_and_bound(graph, start, goal):
    queue = [(0, start, [start])]
    best_cost = float('inf')
    best_path = None

    while queue:
        (cost, node, path) = heapq.heappop(queue)
        
        if node == goal:
            if cost < best_cost:
                best_cost = cost
                best_path = path
            continue
        
        if cost >= best_cost:
            continue
        
        for neighbor, edge_cost in graph[node].items():
            if neighbor not in path:
                new_cost = cost + edge_cost
                new_path = path + [neighbor]
                heapq.heappush(queue, (new_cost, neighbor, new_path))

    return best_path, best_cost

# Example usage
print(branch_and_bound(graph, 'S', 'G'))
