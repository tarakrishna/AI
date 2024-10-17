def alpha_beta(depth, node_index, is_maximizing, leaf_values, alpha, beta):
    if depth == 2:
        return leaf_values[node_index]
    
    if is_maximizing:
        max_score = float('-inf')
        for i in range(2):  
            score = alpha_beta(depth + 1, node_index * 2 + i, False, leaf_values, alpha, beta)
            max_score = max(max_score, score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break  
        return max_score
    else:
        min_score = float('inf')
        for i in range(2): 
            score = alpha_beta(depth + 1, node_index * 2 + i, True, leaf_values, alpha, beta)
            min_score = min(min_score, score)
            beta = min(beta, score)
            if beta <= alpha:
                break  
        return min_score

if __name__ == "__main__":
    leaf_values = [4, 8, 9, 3, 2, -2, 9, 1]

    alpha = float('-inf')
    beta = float('inf')
    optimal_value = alpha_beta(0, 0, True, leaf_values, alpha, beta)
    print(f"The optimal value after the pruning process is {optimal_value}")
