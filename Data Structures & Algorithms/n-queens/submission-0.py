class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = ["." * n for i in range(n)]
        posDiag = set()
        negDiag = set()
        cols = set()
        def backtrack(row):
            nonlocal cols, posDiag, negDiag
            if row == n:
                return True

            for col in range(n):
                pd = col + row
                nd = row - col
                if col not in cols and pd not in posDiag and nd not in negDiag:
                    cols.add(col)
                    posDiag.add(pd)
                    negDiag.add(nd)
                    board[row] = "." * col + "Q" + "." * (n - col - 1)

                    if(backtrack(row + 1)):
                        result.append(board.copy())

                    cols.remove(col)
                    posDiag.remove(pd)
                    negDiag.remove(nd)   
                    board[row] = '.' * n
                    
            return False

        backtrack(0)
        return result