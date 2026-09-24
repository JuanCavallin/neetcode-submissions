from collections import deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        result = []
        graph = {}
        for i in range(len(equations)):
            start, end = equations[i]
            if start not in graph:
                graph[start] = []
            graph[start].append([end, values[i]]) 
            if end not in graph:
                graph[end] = []
            graph[end].append([start, 1 / values[i]])
        
        
        def dfs(node, val, target):
            if node not in graph:
                return -1
            if node == target:
                return val
            if node in path:
                return -1
            path.add(node)
            for neighbor in graph[node]:
                next = dfs(neighbor[0], val * neighbor[1], target)
                if next != -1:
                    return next
            path.remove(node)
            return -1

        for start, end in queries:
            # Run DFS from start to end
            path = set()
            result.append(dfs(start, 1, end))
        return result

