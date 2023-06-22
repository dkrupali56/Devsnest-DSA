def solve(n, nums):
    # CODE HERE
    #stk = [nums[-1]] #increasing stack from rear end of nums
    fallstart = n-1
    
    for i in range(n-2,-1,-1):
        if nums[i]<nums[fallstart]:#stk[-1]:
            break
        fallstart = i#stk.append(nums[i])
        
    if fallstart==0:#len(stk)==n:
        for ind in range(n//2):
            nums[i],nums[n-1-i] = nums[n-1-i],nums[i]
    else:
        new_ind = fallstart#maxval = stk[-1]
        while new_ind<n and nums[new_ind]>nums[i]:
            new_ind+=1#maxval = stk.pop()
        new_ind-=1
        '''
        swap nums[i],nums[new_ind]
        reverse nums[fallstart: ] #fallstart = i+1
        '''
        #print('stk = ',stk,' i = ',i)
        #new_ind = n-len(stk)-1
        nums[i],nums[new_ind] = nums[new_ind],nums[i]
        for ind in range(fallstart, 1 + (fallstart + n-1)//2):
            nums[ind],nums[(n-1)-(ind-fallstart)] = nums[(n-1)-(ind-fallstart)],nums[ind]
    return nums
