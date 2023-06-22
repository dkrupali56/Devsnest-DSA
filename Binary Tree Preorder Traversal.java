static int[] solve(TreeNode root){
   ArrayList<Integer> list=new ArrayList<>();
   
   Preorder(root,list);
   int[] ans=new int[list.size()];
   for(int i=0;i<list.size();i++){
       ans[i]=list.get(i);
   }
   return ans;
}

public static void Preorder(TreeNode root,ArrayList<Integer> ans){
      if(root==null) return ;

      ans.add(root.val);

      Preorder(root.left,ans);
      Preorder(root.right,ans);
}
