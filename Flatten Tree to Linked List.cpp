TreeNode* Global=NULL;
TreeNode* solve(TreeNode* root){
//CODE HERE 
if(!root)
return NULL;
solve(root->right);
solve(root->left);
root->left=NULL;
root->right=Global;
Global=root;
return root;
}
