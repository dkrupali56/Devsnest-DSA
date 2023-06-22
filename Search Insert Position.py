def solve(n, nums, target):
    # CODE HERE 
    if target in nums:
        return nums.index(target) 
    else: 
        for i in range(len(nums)): 
            if nums[i] > target: 
                return i

    return len(nums)
