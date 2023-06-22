def f(i,j,height,res,n,m,vis,e):
    if (i<0 or i>=n or j<0 or j>=m or (i,j) in vis or abs(height[i][j]-e)>res) :
        return False

    if (i == n-1 and j == m-1):
        return True

    vis.add((i,j))

    return f(i+1,j,height,res,n,m,vis,height[i][j]) or f(i-1,j,height,res,n,m,vis,height[i][j]) or f(i,j+1,height,res,n,m,vis,height[i][j]) or f(i,j-1,height,res,n,m,vis,height[i][j])

def solve(height):
    # CODE HERE
    l ,r = 0,10**6
    n,m = len(height), len(height[0])
    res = 0
    ans = 10**6

    while l<=r:
        res = (l+r)//2
        vis = set()
        if (f(0,0,height,res,n,m,vis,height[0][0])):
            ans = res
            r = res - 1
        else : 
            l = res + 1


    return ans
