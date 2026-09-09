class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #Create the graph
        graph = [[] for x in range(len(edges) + 1)]

        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)
        # Do DFS solution for fun then go back an dlearn the union join optimal solution
        visited = set()
        cycle = set()
        cycle_start = None

        def dfs(node, prev):
            nonlocal cycle_start

            if node in visited: 
                # Found a repeated edge, need to return the last edge
                cycle_start = node
                return True
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor == prev:
                    continue
                if dfs(neighbor, node): #Found the start of the cycle, this is the windback part of the code
                #When unwinding we care about the current node not neighbor
                    if cycle_start is not None:
                        cycle.add(node)
                    
                    if node == cycle_start:
                        cycle_start = None
                    

                    return True
            return False

        dfs(1, 0)
        #Have to go through edges and return the first occurance that matches
        for first, second in reversed(edges):
            if first in cycle and second in cycle:
                return [first, second]
        return []



        
            
