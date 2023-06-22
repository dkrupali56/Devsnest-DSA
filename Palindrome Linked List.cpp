Node* cutinhalf(Node* head){
    if(head==NULL || head->next==NULL)return NULL;
    Node* slow=head;
    Node* fast=head;
    while(fast->next && fast->next->next){
        slow=slow->next;
        fast=fast->next->next;
    }
    Node* temp=slow->next;
    slow->next=NULL;
    return temp;
}

Node* reverse(Node* head){
if(head==NULL||head->next==NULL){
    return head;
}
Node* newhead=reverse(head->next);
head->next->next=head;
head->next=NULL;
return newhead;
}

int solve(Node* head){
//CODE HERE 
int ans=1;
Node* sechalf=cutinhalf(head);
sechalf=reverse(sechalf);
Node* firhalf=head;
while(sechalf){
    if(sechalf->data!=firhalf->data){
        ans=0;
    }
    sechalf=sechalf->next;
    firhalf=firhalf->next;
}
return ans;
}
