def solve(n, trust):
    d={}
    for e in trust:
        if e[0] in d :
            d[e[0]]+=1
        if e[0] not in d:
            d[e[0]]=1
        if e[1] not in  d:
            d[e[1]]=0
        if d[e[1]] in d and not d[e[1]] :
            d[e[1]]+=1
        
    for k,v in d.items():
        if v==0:
            return k

    return -1
