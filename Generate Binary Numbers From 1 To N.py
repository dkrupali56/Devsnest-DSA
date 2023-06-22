def decToBin(num): 
    i=0 
    res=0
    while(num>0):
        d = num%2 
        res += d * (10**i) 
        i+=1 
        num//=2 
    return (res)

def solve(n): 
    # CODE HERE 
    my_list = [] 
    for i in range(1,n+1):
        my_list.append(decToBin(i))
    return my_list
