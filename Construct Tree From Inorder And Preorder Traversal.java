static int n;
static TreeNode solve(int n1, int n2, int[] preorder, int[] inorder){
    n=0;
    HashMap<Integer,Integer> map=new HashMap<>();
    for(int i=0;i<inorder.length;i++){
       map.put(inorder[i],i);
    }
    return Inorder(preorder,inorder,map,0,preorder.length-1);
}
public static TreeNode Inorder(int[] preorder,int[] inorder,HashMap<Integer,Integer> map,int start,int end){
    if(n>=preorder.length) return null;
    if(start>end) return null;

    TreeNode node=new TreeNode(preorder[n]);
    int position=map.get(preorder[n]);
    n++;
    node.left=Inorder(preorder,inorder,map,start,position-1);
    node.right=Inorder(preorder,inorder,map,position+1,end);

    return node;
}
