import sys
sys.setrecursionlimit(10**6)
dummyNode=TreeNode(-1)

def solve(root, target):
    if root is None:
        return dummyNode

    if  root.val==target:
        return root
    
    return solve(root.left,target) if root.val>target else solve(root.right,target)
