void preorder(TreeNode* root,vector<int> &res){
    if(root==NULL){
        return;
    }
    if(root->left==NULL && root->right==NULL){
        res.push_back(root->val);
    }
    preorder(root->left,res);
    preorder(root->right,res);
}
int solve(TreeNode* root1, TreeNode* root2){
    vector<int> ans1,ans2;
    preorder(root1,ans1);
    preorder(root2,ans2);
    if(ans1.size()!=ans2.size()){
        return 0;
    }
    for(int i=0;i<ans1.size();i++){
        if(ans1[i]!=ans2[i]){
            return 0;
        }
    }
    return 1;
}
