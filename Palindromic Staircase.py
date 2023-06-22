def solve(n):
    # CODE HERE
    l=[]
    for i in range(1,n+1):
        s=""
        c=""
        for j in range(1,i+1):
            s=s+str(j)
        for k in range(i-1,0,-1):
            c=c+str(k)
        l.append(s+c)
    return l
