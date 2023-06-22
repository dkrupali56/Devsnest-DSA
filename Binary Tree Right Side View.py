def f(node,lvl,st):
    if node :
        if lvl==len(st):
            st.append(node.val)
        f(node.right,lvl+1,st)
        f(node.left,lvl+1,st)

    return st

def solve(root):
    st=[]
    if not root :return st
    return f(root,0,st)
