import heapq

class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        directions = [
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1]
        ]
        result = float('inf')
        heap = []
        visited = {} # (r, c) --> effort
        visited[(0, 0)] = 0
        heap.append((0, 0, 0))
        while heap:
            prevEffort, row, col = heapq.heappop(heap)
            if row == len(heights) - 1 and col == len(heights[row]) - 1:
                result = min(prevEffort, result)
                continue
            for d in directions:
                r = d[0] + row
                c = d[1] + col
                if r < 0 or c < 0 or r >= len(heights) or c >= len(heights[0]):
                    continue
                effort = max(prevEffort, abs(heights[row][col] - heights[r][c]))
                if (r, c) in visited and visited[r, c] <= effort:
                    continue
                heapq.heappush(heap, (effort, r, c))
                visited[(r, c)] = effort
        
        return result