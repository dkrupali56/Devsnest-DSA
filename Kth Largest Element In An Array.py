from heapq import *
def solve(n, nums, k):
    heap = nums[:k]
    heapify(heap)
    for i in range(k,n):
        if nums[i] > heap[0]:
            heapreplace(heap,nums[i])
    return heap[0]
    nums.sort()
    return nums[len(nums)-k]
