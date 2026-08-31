class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        //Need to do multi-source BFS from each treasure chest, then update the next reachable cells that it finds by init + 1 and only push if equals to inf to avoid data storage

        queue<pair<int, int>> q;
        for(int i = 0; i < grid.size(); i++) {
            for(int j = 0; j < grid[i].size(); j++) {
                if(grid[i][j] == 0) {
                    q.push({i, j});
                }
            }
        }

        vector<pair<int, int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while(q.size() > 0) {
            int l = q.size();
            for(int i = 0; i < l; i++) {
                auto current = q.front();
                q.pop();
                for(auto& dir: directions) {
                    int r = current.first + dir.first;
                    int c = current.second + dir.second;

                    if(r >= 0 && r < grid.size() && c >= 0 && c < grid[0].size() 
                    && grid[r][c] == INT_MAX) {
                        q.push({r, c});
                        grid[r][c] = grid[current.first][current.second] + 1;
                    }
                }

            }
        }
    }
};
