Node* cutinhalf(Node* head){
    if(head==NULL || head->next==NULL)return NULL;
    Node* slow=head;
    Node* fast=head;
    while(fast->next && fast->next->next){
        slow=slow->next;
        fast=fast->next->next;
    }
    if(fast->next){
        slow=slow->next;
    }
    Node* temp=slow->next;
    slow->next=NULL;
    return temp;
}
//recursive reverse function
Node* reverse(Node* head){
if(head==NULL||head->next==NULL){
    return head;
}
Node* newhead=reverse(head->next);
head->next->next=head;
head->next=NULL;
return newhead;
}

Node* solve(Node* head){
//CODE HERE 
Node* sechalf=cutinhalf(head);
sechalf=reverse(sechalf);
Node* p=head;
while(sechalf){
    Node* x=sechalf->next;
    sechalf->next=p->next;
    p->next=sechalf;
    p=p->next->next;
    sechalf=x;
}
return head;
}
