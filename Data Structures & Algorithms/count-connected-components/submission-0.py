class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        count = 0

        #Create adjacency list
        graph = [[] for i in range(n)]
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)

        def bfs(node):
            if node in visited:
                return
            queue = deque()
            current = node
            visited.add(current)
            queue.append(current)
            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
                
        
        for i in range(n):
            if i not in visited:
                count += 1
                bfs(i)
        return count

                
        