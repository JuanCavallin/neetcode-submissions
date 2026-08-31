class Solution {
public:

    void islandsAndTreasure(vector<vector<int>>& grid) {
        //Mistake: tried doing DFS because I confused this problem with trying to find all the paths. Finding the shortest for each is not the same as exploring every path. For shortest it is always BFS which is the case with this problem

        //Instead of creating unordered set, reuse existing grid structure
        //Hint in the problem: do not have to touch cells that it would be unable to reach anyway, so very clear solution
        queue<pair<int, int>> q;
        for(int i = 0; i < grid.size(); i++) {
            for(int j = 0; j < grid[i].size(); j++) {
                if(grid[i][j] == 0) {
                    q.push({i, j});
                }
            }
        }

        //BFS logic
        vector<pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        while(q.size() > 0) {
            int k = q.size();
            for(int i = 0; i < k; i++) {
                pair<int, int> current = q.front();

                int row = current.first;
                int col = current.second;
                q.pop();
                for(auto& dir: directions) {
                    int r = row + dir.first;
                    int c = col + dir.second;

                    //ERROR: forgot  to check bounds
                    if(r < 0 || r >= grid.size() || c < 0 || c >= grid[0].size()) {
                        continue;
                    }
                    if(grid[r][c] == INT_MAX) {
                        //SIMPLIFICATION: adjust number as soon as I find instead of using level variable
                        q.push({r, c});
                        grid[r][c] = grid[row][col] + 1;
                    }
                }

            }
        }
    }
};
