class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Need to check that there aren't any cycles in this graph 
        visited = set()
        global_visited = set()
        graph = [[]for i in range(n)] # Same efficiency to use a vector or dictionary if you already know the size and idx maches 1:1 with node
        #Fill the graph
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)

        def dfs(node, previous):
            #Since the graph is undirected, visited but being the previous node is fine, so have to keep track of the correct order
            if node in visited:
                return False
            if graph[node] == []:
                return True
            visited.add(node)
            global_visited.add(node)
            for neighbor in graph[node]:
                if neighbor == previous:
                    continue
                if not dfs(neighbor, node):
                    return False
            visited.remove(node)
            return True

        if dfs(0, -1) and len(global_visited) == n:
            return True
        return False            
            