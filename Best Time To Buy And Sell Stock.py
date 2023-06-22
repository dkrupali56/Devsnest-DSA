def solve(n, prices): 
    # CODE HERE 
    buy = prices[0] 
    max_profit = 0 
    for i in range(1, n):
        if (buy > prices[i]):
            buy = prices[i]
        elif (prices[i] - buy > max_profit):
            max_profit = prices[i] - buy
    return max_profit
