def solve(str1):
    # CODE HERE
    s=[]
    l=[]
    for i in range(0,len(str1)):
        if str1[i] in s:
            pass
        else:
            l.append(str1.count(str1[i]))
            s.append(str1[i])
    return l
