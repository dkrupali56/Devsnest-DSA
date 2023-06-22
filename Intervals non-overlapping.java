static int solve(int[][] interval){
      int ans=0;
      int[] previous=new int[2];
       Arrays.sort(interval,(a,b) -> a[0]-b[0]);
      previous=interval[0];
 
      for(int i=1;i<interval.length;i++){
           
           if(interval[i][0]<previous[1]){
               ans++;
               if(interval[i][1]<previous[1]){
                   previous=interval[i];
               }
           }else{
               previous=interval[i];
           }
      }
  
     return ans;
}
