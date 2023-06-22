def solve(root):
    # CODE HERE
    if root:
        return 1 + max(solve(root.left),solve(root.right))
    return 0
