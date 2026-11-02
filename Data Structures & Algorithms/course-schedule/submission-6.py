class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(set)
        for a, b in prerequisites:
            graph[a].add(b)
        
        
        # my mistake: I defaulted to BFS because it is easier to write vs recursive function but did not take into account that DFS is better suited for tracking path and cycle detection
        path = set()
        def dfs(root):
            if root in path:
                return False
            path.add(root)
            for neighbor in graph[root]:
                if not dfs(neighbor):
                    return False
            path.remove(root)
            graph[root] = set()
            return True
            
            

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


