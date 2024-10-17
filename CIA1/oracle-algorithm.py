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

def oracle_algorithm(graph, start, goal):
    # In a real-world scenario, the Oracle would have perfect knowledge.
    # Here, we'll simulate that by hard-coding the optimal path.
    optimal_path = ['S', 'A', 'D', 'G']
    optimal_cost = sum(graph[optimal_path[i]][optimal_path[i+1]] for i in range(len(optimal_path)-1))
    
    return optimal_path, optimal_cost

# Example usage
print(oracle_algorithm(graph, 'S', 'G'))
