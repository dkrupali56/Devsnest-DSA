def solve(root):
    # CODE HERE
    res = []
    inorder(root, res)
    return res
def inorder(root, ans):
    if not root:
        return 
    if root:
        inorder(root.left, ans)
        ans.append(root.val)
        inorder(root.right, ans)
