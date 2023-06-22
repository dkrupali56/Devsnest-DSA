int sum=0;
TreeNode* solve(TreeNode* root){
//CODE HERE 
if(!root)
return NULL;
solve(root->right);
// update the Node
root->val+=sum;
// update the Sum 
sum=root->val;
solve(root->left);
return root;
}
