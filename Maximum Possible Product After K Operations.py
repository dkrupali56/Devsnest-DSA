from heapq import *
from functools import reduce
def solve(n, nums, k):
    
    mod = (10**9) +7

    heapify(nums)

    while k>0:

        x =  nums[0]

        heapreplace(nums,x+1)

        k -= 1

    return reduce(lambda x,y:(x*y)%mod,nums)
