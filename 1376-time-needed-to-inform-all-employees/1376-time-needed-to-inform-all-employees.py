class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: list[int], informTime: list[int]) -> int:
        graph = defaultdict(list)
        queue = deque([(headID, 0)])
        for i in range(len(manager)):
            graph[manager[i]].append(i)

        result = 0
        while queue:
            current, time = queue.popleft()
            result = max(result, time)
            for neighbor in graph[current]:
                queue.append((neighbor, time + informTime[current]))
                
        return result