from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for start, end in prerequisites:
            graph[start].append(end)
        
        result = []
        can_reach = defaultdict(set)

        def dfs(node, target, start):
            if node == target:
                return True
            if target in can_reach[node]:
                return True
            if node not in graph:
                return False #Not a real conditon but sitll leave in 
            if node in path:
                return False
            path.add(node)
            for neighbor in graph[node]:
                can_reach[start].add(neighbor)
                #can_reach[node].add(neighbor)
                if dfs(neighbor, target, start):
                    return True
            path.remove(node)
            can_reach[node].add(can_reach[start]).remove(node)
            return False
        
        for i in range(len(queries)):
            path = set() #do I actually need for this problem ???? TODO
            if dfs(queries[i][0], queries[i][1], queries[i][0]):
                result.append(True)
            else:
                result.append(False)
            #can_reach[queries[i][0]].append(path)
        
        return result