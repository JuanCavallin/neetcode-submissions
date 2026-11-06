class Solution:
    def buildMatrix(self, k: int, rowConditions: list[list[int]], colConditions: list[list[int]]) -> list[list[int]]:
        result = [[0] * k for i in range(k)]

        # Full BFS Kahns shit for rows
        inDegree = {i: 0 for i in range(1, k + 1)}
        graph = defaultdict(list)
        queue = deque()
        rowOrder = []

        for above, below in rowConditions:
            inDegree[below] += 1
            graph[above].append(below)

        for i in range(1, k + 1):
            if inDegree[i] == 0:
                queue.append(i)
        
        if not queue:
            return []
        
        while queue:
            current= queue.popleft()
            rowOrder.append(current)
            for neighbor in graph[current]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)
        if len(rowOrder) != k:
            return []        
        
        inDegree = {i: 0 for i in range(1, k + 1)}
        graph = defaultdict(list)
        queue = deque()
        colOrder = []

        for above, below in colConditions:
            inDegree[below] += 1
            graph[above].append(below)

        for i in range(1, k + 1):
            if inDegree[i] == 0:
                queue.append(i)
        
        if not queue:
            return []
        
        while queue:
            current= queue.popleft()
            colOrder.append(current)
            for neighbor in graph[current]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)
        if len(colOrder) != k:
            return [] 
        
        # TODO: build the result
        rowPos = {num: i for i, num in enumerate(rowOrder)}
        colPos = {num: i for i, num in enumerate(colOrder)}

        for i in range(1, k + 1):
            r = rowPos[i]
            c = colPos[i]
            result[r][c] = i

        return result
        