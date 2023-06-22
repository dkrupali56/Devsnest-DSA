def solve(n, arr):
    # CODE HERE
    l=[]
    for i in range(0,n+2):
        if i not in arr:
            l.append(i)
    return l;
