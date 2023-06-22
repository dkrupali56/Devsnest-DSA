static Node solve(Node head, int k){
    if(head==null || k==0) return head;
    int size=1;
    Node curr=head;
    while(curr.next!=null){
        curr=curr.next;
        size++;
    } 
    curr.next=head;
    k= k%size;
    for(int i=0;i<size-k;i++){
        curr=curr.next;
    }
    head=curr.next;
    curr.next=null;
    return head;
}
