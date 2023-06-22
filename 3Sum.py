def solve(n, arr):

    ret=[]
    
    arr.sort()

    if arr[0]>0 or arr[-1]<0 or n<3:
        return []

    for i in range(n-2):
        
        if arr[i]>0:
            break

        if i==0 or i>0 and arr[i]!=arr[i-1]:

            low=i+1

            high=len(arr)-1

            req_sum = 0-arr[i]

            while low <high:

                if arr[low]+arr[high]>req_sum:
                    high-=1

                elif arr[low]+arr[high]<req_sum:
                    low+=1

                else:
                    ret.append([-req_sum,arr[low],arr[high]])
                    low+=1
                    high-=1

                    while arr[low]==arr[low-1] and low <high:
                        low+=1

                    while arr[high]==arr[high+1] and low <high:
                        high-=1
                    

    return ret
