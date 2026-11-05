class Solution:
    def shortestPathAllKeys(self, grid: list[str]) -> int:
        key = set() # { [r, c]}
        start = None
        numKeys = 0
        directions = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1]
        ]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j] == '@'):
                    start = (i, j)
                if(grid[i][j] in 'abcdef'):
                    numKeys += 1

        queue = deque()      # r, c, keys unlocked with tuple (1,1,1,1,1,1), dist
        queue.append((start[0], start[1], frozenset(), 0))
        visited = {(start[0], start[1], frozenset())} # r, c, keys
        while queue:
            row, col, keys, dist = queue.popleft()
            if len(keys) == numKeys:
                return dist

            for d in directions:
                r = row + d[0]
                c = col + d[1]
                
                if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                    continue
                
                if grid[r][c] == '#':
                    continue
                if grid[r][c] in "ABCDEF" and grid[r][c].lower() not in keys:
                    continue                
                newKeys = keys
                if grid[r][c] in 'abcdef':
                    newKeys = keys | {grid[r][c]}

                if (r, c, newKeys) in visited:
                    continue
                queue.append((r, c, newKeys, dist + 1))
                visited.add((r, c, newKeys))

        return -1