vector<int> v;
TreeNode* solve(TreeNode* root){
  if(root){
      solve(root->left);
      v.push_back(root->val);
      solve(root->right);
  }
 
  if(v.size()==0) return NULL;
  TreeNode* n=new TreeNode(v[0]);
  TreeNode*h=n;
  if(v.size()==1) return n;
  for(int i=1;i<v.size();i++){
      n->right=new TreeNode(v[i]);
      n=n->right;
  }
  return h;
}
