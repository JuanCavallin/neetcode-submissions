class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = {}
        result = 0
        def find(a):
            if a not in parent:
                parent[a] = a
                return a
            if parent[a] == a:
                return a
            return find(parent[a])
        
        def union(a, b):
            if a not in parent:
                parent[a] = a
            if b not in parent:
                parent[b] = b
            
            rootA, rootB = find(a), find(b)
            parent[rootA] = rootB
        
        for a, b in edges:
            union(a, b)
        
        prev = set()
        for i in range(n):
            root = find(i)
            if root not in prev:
                prev.add(root)
                result += 1
        return result
