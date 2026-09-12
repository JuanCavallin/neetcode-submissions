class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Minimum time = BFS
        #First, create the graph that has all of the nodes that a graph can go to from its point with the time weight
        graph = [[]for i in range(n + 1) ]
        for edge in times:
            graph[edge[0]].append([edge[1], edge[2]])

        #Perform Djikstras, use minheap to get greedy next path, then take the max of the distances and return, unless there is still an unvisited node (return -1)
        distances = [float('inf')] * (n + 1)
        distances[k] = 0 #should I do distances[k] = 0 ? 
        minHeap = [(0, k)] #keep time first since sorting by time for path
        while minHeap:
            time, current = heapq.heappop(minHeap)
            if time > distances[current]:
                continue
            for neighbor in graph[current]:
                newTime = time + neighbor[1]
                if newTime < distances[neighbor[0]]:
                    distances[neighbor[0]] = newTime
                    heapq.heappush(minHeap, (newTime, neighbor[0]))

        if max(distances[1:]) == float('inf'):
            return -1

        return max(distances[1:])
        




