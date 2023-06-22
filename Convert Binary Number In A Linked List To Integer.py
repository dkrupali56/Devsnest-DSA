def solve(head):
    # CODE HERE
    num=0 
    while(head): 
        num=(num*2)+head.data 
        head=head.next 
    return num
