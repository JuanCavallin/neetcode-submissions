class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroFirstRow = False
        zeroFirstCol = False
        #Check if there is a zero in first row or col before proceeding with marking
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                zeroFirstCol = True
                break

        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                zeroFirstRow = True
                break

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 0:
                    # set row
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    # set col

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0


        if zeroFirstRow:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

        if zeroFirstCol:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        

        