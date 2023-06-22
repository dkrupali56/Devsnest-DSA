int solve(vector<vector<int>> points){
    vector<vector<int>> dist;
    int n=points.size();
    priority_queue <vector<int>, vector<vector<int>>, greater<vector<int>> > pq;
    for(int i=0;i<n;i++){
        for(int j=i+1;j<n;j++){
            int dist=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]);
            pq.push({dist,i,j});
        }
    }
    vector<int> par(1001);
    for(int i=0;i<1001;i++){
        par[i]=i;
    }
    int mstsum=0;
    while(n>1){
        vector<int> temp=pq.top();
        pq.pop();
        int d=temp[0];
        int i=temp[1];
        int j=temp[2];
        int par_i=par[i];
        int par_j=par[j];
        while(par[par_i]!=par_i){
            par_i=par[par_i];
        }
        while(par[par_j]!=par_j){
            par_j=par[par_j];
        }
        if(par_i!=par_j){
            par[par_i]=par_j;
            n-=1;
            mstsum+=d;
        }
    }
    return mstsum;
}
