def solve(head, n):
    if not head.next:
        return head
    p1 =p2= head
    for i in range(n):
        p1 = p1.next
    if not p1:
        return head.next
    while p1.next:
        p1 = p1.next
        p2 = p2.next
    p2.next = p2.next.next
    return head
