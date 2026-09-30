class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = {}
        result = n
        def find(a):
            if a not in parent:
                parent[a] = a
                return a
            if parent[a] == a:
                return a
            parent[a] = find(parent[a])
            return parent[a]
        
        def union(a, b):
            nonlocal result
            if a not in parent:
                parent[a] = a
            if b not in parent:
                parent[b] = b
            
            rootA, rootB = find(a), find(b)
            if rootA != rootB:
                result -= 1
                parent[rootA] = rootB
        
        for a, b in edges:
            union(a, b)

        return result
