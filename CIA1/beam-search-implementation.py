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

def beam_search(graph, start, goal, heuristics, beam_width=2):
    beam = [(heuristics[start], start, [start])]
    
    while beam:
        new_beam = []
        for _, node, path in beam[:beam_width]:
            if node == goal:
                return path
            
            for neighbor in graph[node]:
                if neighbor not in path:
                    h = heuristics[neighbor]
                    new_path = path + [neighbor]
                    heapq.heappush(new_beam, (h, neighbor, new_path))
        
        beam = new_beam
    
    return None

# Example usage
print(beam_search(graph, 'S', 'G', heuristics))
