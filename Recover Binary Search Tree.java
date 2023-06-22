static TreeNode solve(TreeNode root){
//CODE HERE 
ArrayList<TreeNode>list=new ArrayList<>();
inorder(root,list);
int n=list.size();
int i=0;
for(i=1;i<n;i++)
{
    if(list.get(i-1).val>list.get(i).val)
    {
        break;
    }
}
TreeNode temp1=list.get(i-1);
for(i=n-1;i>=0;i--)
{
    if(list.get(i).val<list.get(i-1).val)
    break;
}
TreeNode temp2=list.get(i);
if(temp1==temp2)
  temp2=root;
  int xx=temp1.val;
  temp1.val=temp2.val;
  temp2.val=xx;
  return root;
}

static void inorder(TreeNode root, ArrayList<TreeNode>list)
{
    if(root==null)
    return ;
    inorder(root.left,list);
    list.add(root);
    inorder(root.right,list);
}
