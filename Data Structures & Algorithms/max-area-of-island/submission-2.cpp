class Solution {
public:
        int dfs(int r, int c, vector<vector<int>>& grid) {
            if(r < 0 || c < 0 || r >= grid.size() || c >= grid[r].size()) {
                return 0;
            }
            if(grid[r][c] == 0) {
                return 0;
            }
            grid[r][c] = 0; //mark as visited
            return 1 + 
                dfs(r + 1, c, grid) + 
                dfs(r - 1, c, grid) +
                dfs(r, c + 1, grid) + 
                dfs(r, c - 1, grid);
        }

    int maxAreaOfIsland(vector<vector<int>>& grid) {

        int m = 0;
        for(int i = 0; i < grid.size(); i++) {
            for(int j = 0; j < grid[i].size(); j++) {
                int current = dfs(i, j, grid);
                if(current > m) {
                    m = current;
                }
            }
        }
        return m;

    }
};
