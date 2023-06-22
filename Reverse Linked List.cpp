Node* solve(Node* head, int left, int right){
//CODE HERE 
Node* rt=NULL,*lt=NULL,*p,*q,*r=NULL,*plt=NULL,*nrt=NULL;
        Node* temp=head;
        if(head->next==NULL||left==right){return head;}
        int cnt=1;
        while(temp){
            if(cnt==left-1){
                plt=temp;
            }
            if(cnt==left){
                lt=temp;
            }
            if(cnt==right){
                rt=temp;
            }
            temp=temp->next;
            cnt++;
        }
        nrt=rt->next;
        rt->next=NULL;
        p=lt;
        r=p->next;
        while(r){
            q=r;
            r=q->next;
            q->next=p;
            p=q;
        }
        if(plt){
            plt->next=rt;
            lt->next=nrt;
            return head;
        }
        else{
            lt->next=nrt;
            return rt;
    }
}
