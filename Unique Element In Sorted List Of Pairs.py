def solve(n, nums):
    if n==1:
        return nums[0]
    return solve(n//2,nums[:n//2]) ^ solve(n-n//2,nums[n//2:])
