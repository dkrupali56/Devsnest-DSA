def solve(root):

    def fun(root,res=0):

        if root is None:

            return 0

        res = ( res * 2 ) + root.val

        right=fun( root.right , res)

        left=fun( root.left , res)
        
        if left==right==0:
            return res 
        return left+right

    return fun(root)
