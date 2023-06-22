def solve(n, arr):
    # CODE HERE
    maxSum = -999999
    curSum = 0
    for i in arr:
        curSum+=i
        if curSum > maxSum:
            maxSum = curSum
        if curSum < 0:
            curSum = 0
    return maxSum
