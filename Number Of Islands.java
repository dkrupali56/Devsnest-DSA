static int[] dx={-1,0,1,0};
static int[] dy={0,1,0,-1};
static int solve(int[][] grid){
   int ans=0;

   for(int i=0;i<grid.length;i++){
       for(int j=0;j<grid[0].length;j++){
           if(grid[i][j]==1){
              ans++;
            helper(grid,i,j);
           }
       }
   }
   return ans;
}
static void helper(int[][] grid,int i,int j){
    if(i<0 || j<0 || i>= grid.length || j>=grid[0].length || grid[i][j]==0) return ;

    grid[i][j]=0;
    for(int k=0;k<4;k++){
        helper(grid,i+dx[k],j+dy[k]);
    }
}
