def solve(p, q):
    
    if p is None and q is None:

        return 1

    if not(p) and q or p and not(q):

        return 0
    
    return int(p.val==q.val and solve(p.left,q.left) and solve(p.right,q.right))
