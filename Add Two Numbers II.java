static Node solve(Node l1, Node l2){
//CODE HERE 
    Node n1 = reverse(l1);
    Node n2 = reverse(l2);
    Node dummy = new Node(-1);
    Node dum = dummy;
    int carry  = 0 ;
    while(n1!=null&&n2!=null){
        int s = n1.data + n2.data + carry ;
        carry = s/10;
        int d = s%10;
        dum.next = new Node(d);
        dum = dum.next;
        n1=n1.next;
        n2=n2.next;
    }
    while(n1!=null){
        int s = n1.data + carry ;
        carry = s/10;
        int d = s%10;
        dum.next = new Node(d);
        dum = dum.next;
        n1=n1.next;
    }
    while(n2!=null){
        int s = n2.data + carry ;
        carry = s/10;
        int d = s%10;
        dum.next = new Node(d);
        dum = dum.next;
        n2=n2.next;
    }
    if(carry==1){
        dum.next = new Node(carry);
        dum=dum.next;
    }
    Node h = dummy.next;
    dummy.next = null;
    return reverse(h);
}
static Node reverse(Node h){
    Node p = null;
    Node pt = h;
    while(pt.next!=null){
        Node t = pt.next;
        pt.next = p;
        p=pt;
        pt=t;
    }
    pt.next = p;
    return pt;
}
