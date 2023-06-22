def solve(n, arr):
     # CODE HERE
    maxProduct = arr[0]
    curProd = 1
    for i in range(n):
        curProd*=arr[i]
        if curProd > maxProduct:
            maxProduct = curProd
        if curProd == 0:
            curProd = 1
    curProd = 1
    for i in range(n-1,-1,-1):
        curProd*=arr[i]
        if curProd > maxProduct:
            maxProduct = curProd
        if curProd == 0:
            curProd = 1
    return maxProduct
