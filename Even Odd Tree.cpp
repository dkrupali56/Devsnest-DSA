int solve(TreeNode* root){
    if(root==NULL){
        return 1;
    }
    queue<TreeNode*> q;
    q.push(root);
    int level=0;
    int prev;
    while(!q.empty()){
        int size=q.size();
        if(level%2==0){
            prev=0;
            for(int i=0;i<size;i++){
                auto el = q.front();
                q.pop();
                if(el->val>prev && el->val%2!=0){
                    prev=el->val;
                }
                else{
                    return 0;
                }
                if(el -> left) q.push(el -> left);
                if(el -> right) q.push(el -> right);
            }
        }
        else{
            prev=1000001;
            for(int i=0;i<size;i++){
                auto el = q.front();
                q.pop();
                if(el->val<prev && el->val%2==0){
                    prev=el->val;
                }
                else{
                    return 0;
                }
                if(el -> left) q.push(el -> left);
                if(el -> right) q.push(el -> right);
            }
        } 
        ++level;
    }
    return 1;
}
