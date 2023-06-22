static int solve(int[][] isConnected){

Set<Integer> visSet = new HashSet<>();
int n = isConnected.length;
int provinces = 0;

for(int i=0; i<n ; i++){
    if(visSet.contains(i)){
        continue;
    }
    provinces+=1;
    visSet.add(i);

    Queue<Integer> q = new ArrayDeque<>();
    q.add(i);
    while(q.size()>0){
        int el = q.remove();
        for(int j = 0 ; j< n ;j++){
            if(isConnected[el][j]==1 && !visSet.contains(j)){
                visSet.add(j);
                q.add(j);
            }
        }
    }

}
return provinces;
}
