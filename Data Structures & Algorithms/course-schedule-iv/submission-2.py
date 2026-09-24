from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for start, end in prerequisites:
            graph[start].append(end)
        
        result = []

        def dfs(node, target):
            if node == target:
                return True
            if node not in graph:
                return False #Not a real conditon but sitll leave in 
            if node in path:
                return False
            path.add(node)
            for neighbor in graph[node]:
                if dfs(neighbor, target):
                    return True
            path.remove(node)
            return False
        
        for i in range(len(queries)):
            path = set() #do I actually need for this problem ???? TODO 
            result.append(dfs(queries[i][0], queries[i][1]))
        
        return result