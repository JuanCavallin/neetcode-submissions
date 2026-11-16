class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        result = 0
        visited = set()
        visited.add(0) # add visited idx
        dist = [float('inf')] * len(points)
        dist[0] = 0
        prevIdx = 0
        
        for _ in range(1, len(points)):
            currentMin = float('inf')
            currentIdx = 0
            for i in range(len(points)):
                if i in visited:
                    continue 
                d = distance(points[prevIdx], points[i])
                dist[i] = min(dist[i], d)
                if dist[i] < currentMin:
                    currentIdx = i

                currentMin = min(currentMin, dist[i])
            
            result += currentMin
            visited.add(currentIdx)
            prevIdx = currentIdx

                

        return result