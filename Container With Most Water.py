def solve(n, arr):

    #storing the area of water
    water=0
    
    #defining pointers
    i=0
    j=len(arr)-1
   
    while(i<j):
        height=min(arr[i],arr[j])
        width=j-i
     
        #taking the max value
        water=max(water,height*width)

        #increment/decrement the pointer, whose height is minimum
        if(arr[i]<arr[j]):
            i+=1
        else:
            j-=1
    
    return water
