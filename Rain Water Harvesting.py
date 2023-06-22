def solve(n, height):
    # CODE HERE
    water_trapped = 0
    left_ptr,right_ptr = 0, n-1
    left_max,right_max = 0, 0

    while left_ptr < right_ptr:
        if height[left_ptr] <= height[right_ptr]:
            if left_max <= height[left_ptr]:
                left_max = height[left_ptr]
            else:
                water_trapped+= left_max - height[left_ptr]

            left_ptr+=1
        else:
            if right_max <= height[right_ptr]:
                right_max = height[right_ptr]
            else:
                water_trapped+= right_max - height[right_ptr]

            right_ptr-=1
    
    return water_trapped
