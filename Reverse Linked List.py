def solve(head):
    # CODE HERE
    if head.next == None:
        return head
    head2 = solve (head.next)
    head.next.next = head
    head.next = None

    return head2
