static int solve(TreeNode root, int targetSum){
//CODE HERE 
  if(root==null){   
            return 0;
        }
         if(root.left==null && root.right==null && targetSum==root.val){
             return 1;
         }
        
        if(solve(root.left,targetSum-root.val)==1){
            return 1;
        }else if(solve(root.right,targetSum-root.val)==1){
            return 1;
        }
        return 0;
}
