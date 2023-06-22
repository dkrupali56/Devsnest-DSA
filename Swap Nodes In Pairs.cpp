Node* solve(Node* head){
//CODE HERE 
if(head == NULL || head -> next == NULL) 
    return head;
            
Node* temp; 
temp = head->next; 
        
head->next = solve(head->next->next); 
temp->next = head; 
    return temp;
}
