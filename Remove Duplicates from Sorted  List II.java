static Node solve(Node head){
//CODE HERE 
    if(head==null||head.next==null){
        return head;
    }
    Node dummy = new Node(-1);
    Node prev = dummy;
    prev.next = head;
    Node p = head;
    while(p.next!=null){
        if(p.next!=null&&p.data==p.next.data){
            while(p.next!=null&&p.data==p.next.data){
                p=p.next;
            }
                prev.next=p.next;
        }else{
            prev=prev.next;
        }
        if(p.next!=null)p=p.next;
    }
    return dummy.next;
}
