class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(min(coins), amount + 1):
            for coin in coins:
                if coin > i:
                    continue
                if coin == i:
                    dp[i] = 1
                elif dp[i - coin] != float('inf'):
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]
                