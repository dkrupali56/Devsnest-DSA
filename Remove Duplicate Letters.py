def solve(s):
    last={}
    stack=[]
    for i,ele in enumerate(s):
        last[ele]=i
    check=set()
    for i in range(len(s)):
        if s[i] not in check:
            while len(stack)>0 and stack[-1]>s[i] and last[stack[-1]]>i:
                check.remove(stack.pop())

            stack.append(s[i])
            check.add(s[i])

    return "".join(stack)
