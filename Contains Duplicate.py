def solve(n, arr):
    # CODE HERE
    new_lst = []
    for i in arr:
        if i not in new_lst:
            new_lst.append(i)

    if(len(new_lst) == n):
        return 0
    else:
        return 1
