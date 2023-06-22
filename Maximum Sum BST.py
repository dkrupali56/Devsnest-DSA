maxsum=-4*10**4
def maxbst(root):
    global maxsum
    if root:
        if root.left:
            lh,lt,suml=maxbst(root.left)
        else:
            lh=root
            lt=TreeNode(root.val-1)
            suml=0
        if root.right:
            rh,rt,sumr=maxbst(root.right)
        else:
            rt=root
            rh=TreeNode(root.val+1)
            sumr=0
        if lh and rh:
            if rh.val>root.val>lt.val:
                cursum=suml+sumr+root.val
                maxsum=max(maxsum,cursum)
                return lh,rt,cursum
        return False,False,False

def solve(root):
    # CODE HERE
    global maxsum
    maxbst(root)
    if maxsum<0:
        maxsum=0
    return maxsum
    
