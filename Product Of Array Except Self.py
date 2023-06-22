def solve(n, arr):
    
    prefix=[]
    prefix.append(1)

    suffix=[1 for i in range(n)]

    for i in range(1,n):
        prefix.append(prefix[i-1]*arr[i-1])
    for i in range(n-2,-1,-1):

        suffix[i]=suffix[i+1]*arr[i+1]
        

    for i in range(n):
        prefix[i]*=suffix[i]
    return prefix
