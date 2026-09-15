class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        current = [0] * (n + 1)
        current[1] = 1
        current[2] = 2
        for i in range(3, n + 1):
            current[i] = current[i - 1] + current[i - 2]
        return current[-1]
