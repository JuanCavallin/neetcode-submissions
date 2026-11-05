class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for start, end, price in flights:
            graph[start].append((price, end))
        
        result = float('inf')
        queue = deque()
        queue.append((src, 0, 0))
        visited = {}
        visited[src] = 0
        while queue:
            current, price, dist = queue.popleft()
            if current == dst:
                result = min(result, price)
                continue
            if dist == k + 1:
                continue
            for p, neighbor in graph[current]:
                newPrice = price + p
                if neighbor in visited and visited[neighbor] <= newPrice:
                    continue
                queue.append((neighbor, newPrice, dist + 1))
                visited[neighbor] = newPrice
        
        if result == float('inf'):
            return -1
        
        return result
