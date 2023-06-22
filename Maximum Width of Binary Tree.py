def solve(root):
    curr_lvl=[(root,0)]
    max_width=1

    while curr_lvl!=[]:
        next_lvl=[]
        for node,x in curr_lvl:
            if node.left:
                next_lvl.append((node.left,(2*x)+1))
            if node.right:
                next_lvl.append((node.right,(2*x)+2))
    
        if next_lvl!=[]:
            max_width=max(max_width,next_lvl[-1][1]-next_lvl[0][1]+1)
    
        curr_lvl=next_lvl
    return max_width
