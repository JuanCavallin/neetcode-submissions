class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        directions = [
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1]
        ]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j))
        k = 0
        while queue:
            for i in range(len(queue)):
                x, y = queue.popleft()
                for row, col in directions:
                    r = x + row
                    c = y + col
                    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                        continue
                    if grid[r][c] == 2147483647:
                        queue.append((r, c))
                        grid[r][c] = k + 1
            k += 1
                