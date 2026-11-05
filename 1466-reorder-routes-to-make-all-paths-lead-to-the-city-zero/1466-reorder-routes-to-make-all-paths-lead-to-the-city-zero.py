from collections import deque

class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        changed = 0
        visited = set({0})
        queue = deque()
        queue.append(0)
        graph = defaultdict(list)

        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))

        while queue:
            current = queue.popleft()
            for neighbor, direction in graph[current]:
                if neighbor in visited:
                    continue

                changed += direction
                queue.append(neighbor)
                visited.add(neighbor)
        
        return changed

    
        




        return changed