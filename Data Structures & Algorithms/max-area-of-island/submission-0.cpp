class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int dfs(int r, int c, int current) {
            if(r < 0 || c < 0 || r >= grid.length() || c >= grid[r].length()) {
                return grid[r][c]
            }
            if(grid[r][c] == 0) {
                return 0;
            }
            current++;
            grid[r][c] = 0; //mark as visited
            return max(
                dfs(r + 1, c, current),
                dfs(r - 1, c, current),
                dfs(r, c + 1, current),
                dfs(r, c - 1, current)
                )
        }

        int max = 0;
        for(int i = 0; i < grid.size(); i++) {
            for(int j = 0; j < grid[i].size(); j++) {
                int current = dfs(i, j, grid);
                if(current > max) {
                    max = current;
                }
            }
        }
        return max;

    }
};
