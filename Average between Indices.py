def solve(n, arr, x, y):
    # CODE HERE 
    sum=0 
    for i in range(x,y+1):
         sum=sum+arr[i]

    return sum/(y-x+1)
