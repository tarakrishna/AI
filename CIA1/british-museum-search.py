import itertools

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


def british_museum_search(graph, start, goal):
    all_nodes = list(graph.keys())
    best_path = None
    best_cost = float('inf')

    for path_length in range(1, len(all_nodes) + 1):
        for path in itertools.permutations(all_nodes, path_length):
            if path[0] == start and path[-1] == goal:
                cost = calculate_path_cost(graph, path)
                if cost < best_cost:
                    best_cost = cost
                    best_path = path

    return best_path, best_cost

def calculate_path_cost(graph, path):
    cost = 0
    for i in range(len(path) - 1):
        if path[i+1] in graph[path[i]]:
            cost += graph[path[i]][path[i+1]]
        else:
            return float('inf')  # Invalid path
    return cost

# Example usage
print(british_museum_search(graph, 'S', 'G'))
