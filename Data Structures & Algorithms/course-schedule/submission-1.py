from collections import deque
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        # build the graph
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)
        #print(graph)
        
        path = set()
        # Do not need to use path yet since that is for version 2 where I have to return the path
        def dfs(node):
            if node in path:
                return False #Found a loop
            if node in visited:
                return True #reached the end basically for that iteration

            path.add(node)
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
                visited.add(neighbor)
            path.remove(node)
                
            return True

        for course in range(numCourses):
            if course in visited:
                continue
            if not dfs(course):
                return False
        
        return True
        




