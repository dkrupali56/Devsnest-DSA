def solve(n):
    # CODE HERE
     if n == 1:
         return n
     elif n==0:
         return 1    
     else:
         return (n*solve(n-1))
