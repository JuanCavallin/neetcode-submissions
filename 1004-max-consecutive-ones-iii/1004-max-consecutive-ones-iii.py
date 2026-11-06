class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        result = 0
        vals = [0] * 2 # [zeros, ones]
        l, r = 0, 0
        while r < len(nums):
            vals[nums[r]] += 1
            r += 1
            while vals[0] > k:
                vals[nums[l]] -= 1
                l += 1
            result = max(result, r - l)

        return result