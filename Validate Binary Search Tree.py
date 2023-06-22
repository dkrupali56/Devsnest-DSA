def inorder(root, res):
    if not root:
        return 
    if root:
        inorder(root.left, res)
        res.append(root.val)
        inorder(root.right, res)
def solve(root):
    ans = []
    inorder(root,ans)
    for i in range(1,len(ans)):
        if not (ans[i] > ans[i-1]):
            return 0
    return 1
