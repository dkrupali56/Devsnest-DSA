def fun(root,isleft=False):

    if not(root):
        return 0

    if not(root.left or root.right):
        return root.val if isleft else 0
    
    return fun(root.left,True) + fun(root.right,False)

def solve(root):
    
    return fun(root)
