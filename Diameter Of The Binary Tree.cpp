int res(TreeNode* root,int &ans){
    if(root==NULL){
        return 0;
    }
    int lheight=res(root->left,ans);
    int rheight=res(root->right,ans);
    ans=max(ans,1+lheight+rheight);
    return 1+max(lheight,rheight);;
}
int solve(TreeNode* root){
    int ans=INT_MIN;
    res(root,ans);
    return ans-1;
}
