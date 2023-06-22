def solve(n):
    # CODE HERE
    if(n<=1):
        return n
    else:
        return (solve(n-1)+solve(n-2))
        