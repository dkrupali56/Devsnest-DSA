static Node solve(Node head, int key){
      Node ans=head;
  
      while(ans!=null && ans.data==key){
          ans=ans.next;
      }
       head=ans;
      while(head!=null && head.next!=null){
          if(head.next.data==key){
              head.next=head.next.next;
          }else{
              head=head.next;
          }
      }

      return ans;
}
