def solve(n, nums):
    # CODE HERE
    s=set() 
    for num in nums: 
        if num in s:
            s.remove(num) 
        else:
            s.add(num) 
    return list(s)[0]
