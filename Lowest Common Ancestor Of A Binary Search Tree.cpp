TreeNode* solve(TreeNode* root, int p, int q){
//CODE HERE 
if(!root)
return NULL;

//if Node found return it
if(root->val==p)
return root;
if(root->val==q)
return root;

TreeNode* l=solve(root->left,p,q);
TreeNode* r=solve(root->right,p,q);
// if both side of a node return something it means this is the ancestor 
if(l&&r){
    return root;
}
else if(l)//otherwise pass the root/value coming from down to upward as it is.
return l;
else 
return r;
}
