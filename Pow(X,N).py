def solve(x, n):
    # CODE HERE

    if n<0:
        x=(1/x) 
        n=abs(n)
    if x==0 or n==0:
        return 1
    ans=1
    temp=x
    while n>0:

        if n%2==0:
            temp=temp*temp
            n//=2

        else:
            ans*=temp
            n-=1
        
    return ans
