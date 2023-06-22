def solve(n, nums):
    def the(numb,lst):
        for i in lst:
            if numb<i:
                return i

        return -1
    answer=[]
    nums+=nums
    for i in range(n):
        store=the(nums[0],nums)
        answer.append(store)
        nums.pop(0)
    return answer
