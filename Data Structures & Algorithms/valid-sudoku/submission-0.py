from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Check the row
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[i])):
                #spaces 0 - len(board) = rows
                #spaces len(board) + 1 --> that plus len(board[0]) = cols
                if board[i][j] == '.':
                    continue
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squares[(i // 3, j //3)]:
                    print(i, j)
                    return False
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j]) #using add because these are sets
                    squares[(i // 3, j //3)].add(board[i][j])
                
                #Implement the checks for rows and cols first, then for the smaller squares
                #spaces previous + (i * j) // 9 = square

        return True