def solve(intervals):

    n=len(intervals)

    intervals.sort(key=lambda x:(x[0],x[1]))

    i=0

    ret=[]

    # For Iteration
    while i<n:

        a=intervals[i][0]
        b=intervals[i][1]

        i+=1

        if i>n:
            ret.append([a,b])
            break

        # For Merging
        while i<n and intervals[i][0] <=b:
            b=max(b,intervals[i][1])
            i+=1

        ret.append([a,b])
        #print(i)
    return ret
