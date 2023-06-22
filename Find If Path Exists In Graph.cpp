int solve(int n, vector<vector<int>> edges, int source, int destination){
      vector<vector<int>> graph(n);
         for(int i=0; i<edges.size(); i++) {
            graph[edges[i][0]].push_back(edges[i][1]);
            graph[edges[i][1]].push_back(edges[i][0]);
        }
       
          vector<int> visited(n, 0);
        queue<int>q;                      
        q.push(source);                
        visited[source]=1;               
        while(!q.empty()){            
            int frnt=q.front();         
            q.pop();
            if(frnt==destination) return true;   
            for(int i=0;i<graph[frnt].size();i++){  
                if(visited[graph[frnt][i]]==0){     
                    q.push(graph[frnt][i]);     
                    visited[graph[frnt][i]]=1; 
                }
            }
        }
        return false;
       
    }
