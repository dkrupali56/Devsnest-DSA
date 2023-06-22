def solve(n, nums): 
    # CODE HERE

    n = len(nums)

    result = list()

    

    if n == 0: return result

    currentSum = 0

    for i in range(n):

        currentSum += nums[i]

        result.append(currentSum)

    

    return result
