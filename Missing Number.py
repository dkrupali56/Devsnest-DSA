def solveUsingFormula(n, arr):
    return (n*(n+1))//2 - sum(arr)

def solveUsingXor(n, arr):
    xor = n
    for i in range(n):
        xor = xor ^ i ^ arr[i]
    return xor    

def solve(n, arr):
    # CODE HERE
    return solveUsingFormula(n,arr)
