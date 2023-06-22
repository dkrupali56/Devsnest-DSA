static Node solve(Node l1, Node l2){

//CODE HERE

Node dummyHead = new Node(0);

Node p = l1, q = l2, currNode = dummyHead;

int carry = 0;

while (p != null || q != null) {

    int x = (p != null) ? p.data : 0;

    int y = (q != null) ? q.data : 0;

    int sum = carry + x + y;

    carry = sum / 10;

    currNode.next = new Node(sum % 10);

    currNode = currNode.next;

    if (p != null) p = p.next;

    if (q != null) q = q.next;

}

if (carry > 0) {

    currNode.next = new Node(carry);

}

return dummyHead.next;
}
