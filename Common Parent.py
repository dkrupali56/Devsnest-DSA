def solve(root, p, q):
      
    if root is None or root.val in {p,q}:

        return root
    
    left = solve(root.left,p,q) 

    right = solve(root.right,p,q)
    
    return root if left and right else left or right
