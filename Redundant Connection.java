static int[] solve(int[][] edges){
//CODE HERE 
     int Max_EdgeVal=1000;
    ArrayList<Integer>[] graphes=new ArrayList[Max_EdgeVal+1];
 
    for(int i=0;i<Max_EdgeVal+1;i++){
        graphes[i]=new ArrayList<>();
    }

    for(int[] edge:edges){
        HashSet<Integer> set=new HashSet<>();
        if(!graphes[edge[0]].isEmpty() && !graphes[edge[1]].isEmpty() && DFS(graphes,edge[0],edge[1],set)) return edge;

        graphes[edge[0]].add(edge[1]);
        graphes[edge[1]].add(edge[0]);
    }
   
   return new int[]{};
}
static boolean DFS(ArrayList<Integer>[] graphes,int sour,int dest,HashSet<Integer> set){
    if(set.contains(sour)) return false;
    
    set.add(sour);
    if(sour==dest) return true;
    ArrayList<Integer> list=graphes[sour];
    for(int i=0;i<list.size();i++){
        if(DFS(graphes,list.get(i),dest,set)) return true;
    }

    return false;
}
