Node* solve(Node* head, int x){
    Node* d1 = new Node;
    Node* d2 = new Node;
    Node *p1 = d1, *p2 = d2;
    Node* cur = head;
    while(cur!=NULL){
        Node* nxt = cur->next;
        if(cur->data < x){
            p1->next = cur;
            cur->next = NULL;
            p1 = p1->next;
        }
        //cur->data >= x
        else{
            p2 -> next = cur;
            cur->next = NULL;
            p2 = p2->next;
        }
        cur = nxt;
    }
    if(p1!=NULL){
        p1->next = d2->next;
        return d1->next;
    }
    return d2->next;
}
