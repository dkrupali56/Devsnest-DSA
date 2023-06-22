def solve(root):
    
    if root is None:

        return

    solve(root.left)

    solve(root.right)

    root.left,root.right=root.right,root.left

    return root
