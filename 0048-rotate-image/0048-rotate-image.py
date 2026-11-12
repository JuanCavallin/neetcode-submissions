class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def rotate(left, size):
            for i in range(left, size - 1):
                opposite = size + left - i - 1
                p1 = matrix[left][i]
                p2 = matrix[i][size - 1]
                p3 = matrix[size - 1][opposite]
                p4 = matrix[opposite][left]

                matrix[left][i], matrix[i][size - 1], matrix[size - 1][opposite], matrix[opposite][left] = p4, p1, p2, p3
        
        l = 0
        r = len(matrix)
        while l < r:
            rotate(l, r)
            l += 1
            r -= 1
            