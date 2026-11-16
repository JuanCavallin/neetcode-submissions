class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        result = 0
        l, r = 0, 0
        current = 1
        while r < len(nums):
            current *= nums[r]
            while l < r and current >= k:
                current //= nums[l]
                l += 1
            if current < k:
                result += (r - l + 1)
        
            r += 1
        
        return result