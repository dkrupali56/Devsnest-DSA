def solve2(root, low, high):

    global curr_sum

    if root is None:
        return 0

    if root.val >= low and root.val <= high:
        
        return root.val + solve2(root.left,low,high) +solve2(root.right,low,high)

    return  solve2(root.left,low,high) +solve2(root.right,low,high)

def solve(root, low, high):

    return solve2(root, low, high)
