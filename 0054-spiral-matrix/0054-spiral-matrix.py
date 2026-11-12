class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix:
            return []
        result = []
        x, y = -1, 0
        visited = set()
        def add(x, y):
            if (x, y) in visited:
                return False
            result.append(matrix[y][x])
            visited.add((x, y))
            return True
        def spiral(rows, cols):
            nonlocal x, y
            for i in range(cols):
                x += 1
                if not add(x, y):
                    return True
            for i in range(1, rows):
                y += 1
                if not add(x, y):
                    return True
            for i in range(1, cols):
                x -= 1
                if not add(x, y):
                    return True                    
            for i in range(1, rows - 1):
                y -= 1
                if not add(x, y):
                    return True
            return False
        
        rows = len(matrix)
        cols = len(matrix[0])
        while rows > 0 and cols > 0:
            if spiral(rows, cols):
                return result
            rows -= 2
            cols -= 2
            print(x, y)

        return result
