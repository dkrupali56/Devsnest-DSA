def solve(M, N):
    # CODE HERE
    arr = []
    for i in range(1,M,2): 
        arr.append((i * ".|.").center(N, "-"))
    arr.append("DEVSNEST!".center(N,"-"))
    for i in range(M-2,-1,-2): 
        arr.append((i * ".|.").center(N, "-"))
    return arr
