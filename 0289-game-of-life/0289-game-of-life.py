class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def update(x, y):
            neighbors = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    r = y + i
                    c = x + j
                    if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
                        continue
                    if abs(board[r][c] - 2) == 1:
                        neighbors += 1
                    if neighbors > 3:
                        if board[y][x] == 1:
                            board[y][x] = 3
                        return
            if neighbors == 3 and board[y][x] == 0:
                board[y][x] = 2
            elif board[y][x] == 1 and neighbors not in (2, 3):
                board[y][x] = 3   
     


        for i in range(len(board)):
            for j in range(len(board[i])):
                update(j, i)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 3:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1     