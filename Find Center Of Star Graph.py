def solve(edges):
    # CODE HERE
    mat = [x for edge in edges for x in edge]
    for x in mat:
        if mat.count(x) == len(edges):
            return(x)
