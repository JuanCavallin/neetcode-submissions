class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        visited = set()
        visited.add(0)
        prev = 0
        dist = [float('inf')] * len(points)
        currentIdx = 0
        result = 0

        for _ in range(1, len(points)):
            currentMin = float('inf')
            for i in range(len(points)):
                if i in visited:
                    continue
                d = distance(points[i], points[prev])
                dist[i] = min(dist[i], d)
                if dist[i] < currentMin:
                    currentMin = dist[i]
                    currentIdx = i
            prev = currentIdx
            result += currentMin
            visited.add(currentIdx)
        
        return result

