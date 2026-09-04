class Solution {
private:
    vector<pair<int, int>> directions = {
        {1, 0}, {-1, 0}, {0, 1}, {0, -1}
    };

public:
    void dfs(
        int r,
        int c,
        vector<vector<int>>& ocean,
        vector<vector<int>>& heights
    ) {
        ocean[r][c] = 1;

        for(auto& dir : directions) {
            int row = r + dir.first;
            int col = c + dir.second;

            // Out of bounds
            if(
                row < 0 || row >= heights.size() ||
                col < 0 || col >= heights[0].size()
            ) {
                continue;
            }

            // Already visited for this ocean
            if(ocean[row][col] == 1) {
                continue;
            }

            // Reverse traversal:
            // only move to cells that are >= current height
            if(heights[row][col] < heights[r][c]) {
                continue;
            }

            dfs(row, col, ocean, heights);
        }
    }

    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        vector<vector<int>> result;

        int rows = heights.size();
        int cols = heights[0].size();

        vector<vector<int>> pa(
            rows,
            vector<int>(cols, 0)
        );

        vector<vector<int>> atl(
            rows,
            vector<int>(cols, 0)
        );

        // Start DFS from Pacific and Atlantic borders
        for(int r = 0; r < rows; r++) {
            dfs(r, 0, pa, heights);
            dfs(r, cols - 1, atl, heights);
        }

        for(int c = 0; c < cols; c++) {
            dfs(0, c, pa, heights);
            dfs(rows - 1, c, atl, heights);
        }

        // Cells reachable by both oceans
        for(int r = 0; r < rows; r++) {
            for(int c = 0; c < cols; c++) {
                if(pa[r][c] == 1 && atl[r][c] == 1) {
                    result.push_back({r, c});
                }
            }
        }

        return result;
    }
};