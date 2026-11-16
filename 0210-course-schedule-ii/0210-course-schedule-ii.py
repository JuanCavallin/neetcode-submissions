from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        result = []
        visited = set()
        path = set()

        def dfs(root):
            if root in path:
                return False

            if root in visited:
                return True
            path.add(root)

            for neighbor in graph[root]:
                if not dfs(neighbor):
                    return False

            path.remove(root)
            visited.add(root)
            result.append(root)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return result