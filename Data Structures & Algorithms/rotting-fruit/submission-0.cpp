class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        queue<pair<int, int>> rotten;
        int time = 0;
        int fresh = 0;

        //helper
        vector<pair<int, int>> directions = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}};

        for(int i = 0; i < grid.size(); i++) {
            for(int j = 0; j < grid[i].size(); j++) {
                if(grid[i][j] == 1) {
                    fresh++;
                }
                if(grid[i][j] == 2) {
                    rotten.push({i, j});
                }
            }
        }
        if(fresh > 0 && rotten.size() == 0) {
            return -1;
        }
        if(fresh == 0) return 0; 
        //Run BFS and trackc time
        while(fresh > 0 && rotten.size() > 0) {
            //Track level
            int l = rotten.size();
            for(int k = 0; k < l; k++) {
                auto current = rotten.front();
                rotten.pop();
                for(auto dir : directions) {
                    int r =  current.first + dir.first;
                    int c = current.second + dir.second;

                    if(r >= 0 && r < grid.size() && c >= 0 && c < grid[0].size() && grid[r][c] == 1) {
                        grid[r][c] = 2; //marks as visited
                        rotten.push({r, c});
                        fresh--;
                    }
                }
            }
            time++;
        }
        return fresh == 0 ? time : -1;

    }
};
