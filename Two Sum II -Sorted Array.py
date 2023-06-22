def solve(n, arr, target):
    start=0
    end=n-1

    while start<end:

        if arr[start]+arr[end]==target:
            return [start+1,end+1]

        elif arr[start]+arr[end]>target:
            end-=1
        else:
            start+=1

    return -1
