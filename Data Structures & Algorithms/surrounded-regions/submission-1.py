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
            queue = collections.deque([(r, c)])
            visited.add((r, c))
            global_visited.add((r, c))
            touched_border = False
            while queue:
                current = queue.popleft()
                if current[0] == 0 or current[0] == len(board) - 1 or current[1] == 0 or current[1] == len(board[0]) - 1:
                    touched_border = True
                for dir in directions:
                    row = current[0] + dir[0]
                    col = current[1] + dir[1]
                    if 0 <= row < len(board) and 0 <= col < len(board[0]):
                        if board[row][col] == 'O' and (row, col) not in visited:
                            queue.append((row, col))
                            visited.add((row, col))
                            global_visited.add((row, col))
            if(not touched_border):
                for cell in visited:
                    board[cell[0]][cell[1]] = 'X'

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'O' and (i, j) not in global_visited:
                    bfs(i, j, board)