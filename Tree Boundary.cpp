void traverseleft(TreeNode* root,vector<int> &ans){
    if(root==NULL){
        return;
    }
    if(root->left==NULL && root->right==NULL){
        return;
    }
    ans.push_back(root->val);
    if(root->left){
        traverseleft(root->left,ans);
    }
    else{
        traverseleft(root->right,ans);
    }
}

void traverseleaf(TreeNode* root,vector<int> &ans){
    if(root==NULL){
        return;
    }
    if(root->left==NULL && root->right==NULL){
        ans.push_back(root->val);
        return;
    }
    traverseleaf(root->left,ans);
    traverseleaf(root->right,ans);
}

void traverseright(TreeNode* root,vector<int> &ans){
    if(root==NULL){
        return;
    }
    if(root->left==NULL && root->right==NULL){
        return;
    }
    if(root->right){
        traverseright(root->right,ans);
    }
    else{
        traverseright(root->left,ans);
    }
    ans.push_back(root->val);
}

vector<int> solve(TreeNode* root){
    vector<int> ans;
    if(root==NULL){
        return ans;
    } 
    ans.push_back(root->val);
    traverseleft(root->left,ans);
    traverseleaf(root->left,ans);
    traverseleaf(root->right,ans);
    traverseright(root->right,ans);
    return ans;
}
