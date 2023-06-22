def sf(lroot,rroot):
    if not lroot and not rroot:
        return 1
    
    if (not lroot and rroot) or (lroot and not rroot):
        return 0

    if lroot.val != rroot.val:
        return 0

    return sf(lroot.left, rroot.right) and sf(lroot.right, rroot.left)

def solve(root):
    return sf(root.left, root.right)
