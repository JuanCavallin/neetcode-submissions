class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Run BFS from each of the O cells, check if any of them reach the border and if so stay the same, else recursively swap  
        global_visited = set()
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]

        def bfs(r, c, board):
            #Start with implementing basic dfs
            visited = set()
            queue = []
            current = (r, c)
            queue.append(current)
            visited.add(current)
            touched_border = False
            while(len(queue) > 0 ):
                for dir in directions:
                    row = current[0] + dir[0]
                    col = current[1] + dir[1]
                    if (row, col) in global_visited:
                        continue
                    if(row < 0 or col < 0 or row >= len(board) or col >= len(board[0])):
                        touched_border = True
                        continue
                    if board[row][col] == 'O':
                        queue.append((row, col))
                        visited.add((row, col))
                        global_visited.add((row, col))
                current = queue.pop(0)
            if(not touched_border):
                for cell in visited:
                    board[cell[0]][cell[1]] = 'X'

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'O' and (i, j) not in global_visited:
                    bfs(i, j, board)

