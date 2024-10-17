def minimax(depth, nodeIndex, isMaximizingPlayer, values, alpha, beta):

    if depth == 3:
        return values[nodeIndex]
    
    if isMaximizingPlayer:
        maxEval = float('-inf')
        for i in range(2):  
            eval = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  
        return maxEval
    else:
        minEval = float('inf')
        for i in range(2):  
            eval = minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break 
        return minEval

# Driver code
if __name__ == "__main__":
    values = [1, 4, 7, 2, 3, 0, 6, 5]
    

    alpha = float('-inf')
    beta = float('inf')
    
    optimalValue = minimax(0, 0, True, values, alpha, beta)
    
    print(f"The optimal after the pruning process is {optimalValue}")