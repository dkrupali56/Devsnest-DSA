class node{
    public:
    int x,y,time;
    node(int _x, int _y, int _time){
        x = _x;
        y = _y;
        time = _time;
    }
};

int solve(vector<vector<int>> grid){
    int m = grid.size(), n = grid[0].size();
    int ans = 0;
    int fresh = 0, rotten = 0;
    queue<node> q;
    //Insert all rotten oranges in queue, count Fresh oranges
    for(int i = 0 ; i < m ; i++){
        for(int j = 0 ; j < n ; j++){
            if(grid[i][j] == 1)
                fresh+=1;
            else if(grid[i][j] == 2){
                rotten+=1;
                q.push(node(i,j,0));
            }
        }
    }
    if(fresh==0) return 0;
    int dx[] = {0,1,-1,0};
    int dy[] = {1,0,0,-1};

    while(!q.empty()){
        node ele = q.front();
        q.pop();

        int x = ele.x;
        int y = ele.y;
        int time = ele.time;
        ans = max(ans, time);

        for(int a = 0 ; a < 4 ; a++){
            int nx = x+dx[a];
            int ny = y+dy[a];
            if(nx>=0 && nx<m && ny >= 0 && ny < n && grid[nx][ny] == 1){
                grid[nx][ny] = 2;
                fresh-=1;
                q.push(node(nx, ny, time+1));
            }
        }
        
    }

    if(fresh == 0) return ans;
    return -1;

}
