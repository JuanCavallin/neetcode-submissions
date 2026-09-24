class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        grid = [[0] * (len(text2) + 1) for i in range(len(text1) + 1)]
        
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                prev = max(grid[i + 1][j + 1], grid[i + 1][j], grid[i][j + 1])
                if text1[i] == text2[j]:
                    grid[i][j] = prev + 1
                else:
                    grid[i][j] = prev
        return grid[0][0]

