class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        #inDegree = defaultdict(int)
        if n == 1:
            return [0]

        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        queue = deque()
        for i in range(n):
            if len(graph[i]) == 1:
                queue.append(i)

        remaining = n
        while remaining > 2:
            size = len(queue)
            for i in range(size):
                current = queue.popleft()
                remaining -= 1
                neighbors = graph[current]
                for neighbor in neighbors:
                    graph[neighbor].remove(current)
                    if len(graph[neighbor]) == 1:
                        queue.append(neighbor)
            
        return list(queue)
