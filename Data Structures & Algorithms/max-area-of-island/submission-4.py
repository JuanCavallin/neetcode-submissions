class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        directions = [
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1]
        ]
        visited = set()

        def dfs(x, y):
            if grid[x][y] == 0 or (x, y) in visited:
                return 0
            visited.add((x, y))
            k = 0
            for row, col in directions:
                r = x + row
                c = y + col
                if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                    continue
                k += dfs(r, c)
            return k + 1
            

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    result = max(result, dfs(i, j))


        return result