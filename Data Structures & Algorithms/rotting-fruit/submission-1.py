class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1]
        ]
        result = 0
        fresh = 0
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1

        while queue:
            if fresh == 0:
                return result
            for i in range(len(queue)):
                x, y = queue.popleft()
                for row, col in directions:
                    r = row + x
                    c = col + y
                    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                        continue
                    if grid[r][c] == 1:
                        queue.append((r, c))
                        grid[r][c] -= 1
                        fresh -= 1
            result += 1

        if fresh > 0:
            return -1
        return result
