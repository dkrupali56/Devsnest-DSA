def solve(root):
    even=True
    q=deque()
    q.appendleft(root)
    res=[]
    while q :
        n=len(q)
        ans=[]
        if even :
            for i in range(n):
                ele=q.pop()
                ans.append(ele.val)
                if ele.left:
                    q.appendleft(ele.left)

                if ele.right:
                    q.appendleft(ele.right)

            res.append(ans)

        else :
            for i in range(n):
                ele=q.popleft()
                ans.append(ele.val)
                if ele.right:
                    q.append(ele.right)

                if ele.left:
                    q.append(ele.left)

            res.append(ans)
        
        even=not even

    return res
