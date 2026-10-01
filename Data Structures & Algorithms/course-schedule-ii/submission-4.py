class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
            #graph[b].append(a)
        
        path = set()
        visited = set()
        result = []
        def dfs(root):
            if root in path:
                return False  

            if root in visited:
                return True

            visited.add(root)
            path.add(root)


            for neighbor in graph[root]:
                if not dfs(neighbor):
                    return False # found a cycle so need to exit
            path.remove(root)
            visited.add(root)
            result.append(root)
            return True

        
        for i in range(numCourses):
            if i in visited:
                continue
            if not dfs(i):
                return []
        return result