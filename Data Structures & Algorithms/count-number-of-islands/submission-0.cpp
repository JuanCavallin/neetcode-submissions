class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty()) return 0;

        int rows = grid.size();
        int cols = grid[0].size();
        int islands = 0;

        vector<vector<bool>> visited(rows, vector<bool>(cols, false));

        // Directions: down, up, right, left
        vector<pair<int,int>> directions = {
            {1, 0}, {-1, 0}, {0, 1}, {0, -1}
        };

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {

                if (!visited[i][j] && grid[i][j] == '1') {
                    islands++;

                    // BFS
                    queue<pair<int,int>> q;
                    q.push({i, j});
                    visited[i][j] = true;

                    while (!q.empty()) {
                        auto [r, c] = q.front();
                        q.pop();

                        for (auto [dr, dc] : directions) {
                            int nr = r + dr;
                            int nc = c + dc;

                            // bounds + conditions
                            if (nr >= 0 && nr < rows &&
                                nc >= 0 && nc < cols &&
                                !visited[nr][nc] &&
                                grid[nr][nc] == '1') {

                                visited[nr][nc] = true;
                                q.push({nr, nc});
                            }
                        }
                    }
                }
            }
        }

        return islands;
    }
};
