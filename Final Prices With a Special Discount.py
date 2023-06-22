def solve(n, prices):
    
    stack = []

    for i in range(n-1,-1,-1):
        
        x=prices[i]

        while len(stack) > 0 and stack[-1] > prices[i]:

            stack.pop()

        if stack:
            
            prices[i]  -= stack[-1]

        stack.append(x)
        #print(stack)
    return prices
