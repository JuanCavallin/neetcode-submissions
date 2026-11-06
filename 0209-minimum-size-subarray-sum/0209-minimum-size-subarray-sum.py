class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        result = float('inf')
        l, r = 0, 0
        current = 0

        while r < len(nums):
            current += nums[r]
            r += 1

            while current >= target:
                current -= nums[l]
                result = min(result, (r - l))
                l += 1

        return result if result != float('inf') else 0