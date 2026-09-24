class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        grid = [[0] * (len(word2) + 1) for k in range(len(word1) + 1)]
        for i in range(len(word1)):
            grid[i][-1] = len(word1) - i
        for j in range(len(word2)):
            grid[-1][j] = len(word2) - j

        # Iterate through the grid backwards
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]: #TODO: fix going out of bounds by also entering if either one is larger than the length
                    grid[i][j] = grid[i + 1][j + 1] # same as setting to 0 since already filled
                else:
                    grid[i][j] = min(grid[i + 1][j + 1], grid[i][j + 1], grid[i + 1][j]) + 1
        return grid[0][0]