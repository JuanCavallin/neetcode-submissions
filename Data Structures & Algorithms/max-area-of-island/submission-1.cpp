class Solution {
public:
        int dfs(int r, int c, int current, vector<vector<int>>& grid) {
            if(r < 0 || c < 0 || r >= grid.size() || c >= grid[r].size()) {
                return current;
            }
            if(grid[r][c] == 0) {
                return current;
            }
            current++;
            grid[r][c] = 0; //mark as visited
            return std::max({
                dfs(r + 1, c, current, grid),
                dfs(r - 1, c, current, grid),
                dfs(r, c + 1, current, grid),
                dfs(r, c - 1, current, grid)
        });
        }

    int maxAreaOfIsland(vector<vector<int>>& grid) {

        int m = 0;
        for(int i = 0; i < grid.size(); i++) {
            for(int j = 0; j < grid[i].size(); j++) {
                int current = dfs(i, j, 0, grid);
                if(current > m) {
                    m = current;
                }
            }
        }
        return m;

    }
};
