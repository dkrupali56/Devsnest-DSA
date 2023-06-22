static int[] solve(TreeNode root){
   ArrayList<Integer> list=new ArrayList<>();
   
   Postorder(root,list);
   int[] ans=new int[list.size()];
   for(int i=0;i<list.size();i++){
       ans[i]=list.get(i);
   }
   return ans;
}

public static void Postorder(TreeNode root,ArrayList<Integer> ans){
      if(root==null) return ;

      Postorder(root.left,ans);
      Postorder(root.right,ans);

      ans.add(root.val);
}
