static int solve(int numCourses, int[][] prerequisites){
     HashMap<Integer,ArrayList<Integer>> map=new HashMap<>();

     int[] indegree=new int[numCourses];

     for(int[] arr:prerequisites){
         indegree[arr[0]]++;
         ArrayList<Integer> list=map.getOrDefault(arr[1],new ArrayList<>());
         list.add(arr[0]);
         map.put(arr[1],list);
     }
    
    Queue<Integer> que=new LinkedList<>();
    for(int i=0;i<numCourses;i++){
        if(indegree[i]==0){
            que.add(i);
        }
    }
    int count=0;
    while(que.size()>0){
        int n=que.remove();
        count++;
        ArrayList<Integer> list=new ArrayList<>();
        if(map.containsKey(n)) list=map.get(n);
        for(int i=0;i<list.size();i++){
            if(--indegree[list.get(i)]==0) que.add(list.get(i));
        }
    }

    if(count==numCourses) return 1;
    return 0;
}
