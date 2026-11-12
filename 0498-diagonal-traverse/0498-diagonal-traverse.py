class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        result = []
        def diagonal(x, y):
            temp = []
            while x < len(mat[0]) and y >= 0:
                temp.append(mat[y][x])
                x += 1
                y -= 1
            return temp

        turn = 1
        for i in range(len(mat)):
            turn = abs(turn - 1)
            temp = diagonal(0, i)
            if turn == 1:
                temp.reverse()
            result.extend(temp)
        for i in range(1, len(mat[-1])):
            turn = abs(turn - 1)
            temp = diagonal(i, len(mat) - 1)
            if turn == 1:
                temp.reverse()
            result.extend(temp) 

        return result
