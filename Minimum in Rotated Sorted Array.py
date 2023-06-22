def solve(n, nums):
    # CODE HERE
    start = 0
    end = n-1
    while start < end:
        mid = start + (end - start)//2
        if nums[mid] > nums[end]:
            start = mid + 1
        else:
            end = mid
    
    return nums[start]
