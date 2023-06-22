def solve(n, pages, capacity): 
    q = [] 
    count = 0
    for ans in pages:
        if len(q) == capacity and ans not in q:
            q.pop(0)
            q.append(ans)
            count += 1
        elif len(q) <= capacity and ans not in q:
            q.append(ans)
            count += 1
    return count
