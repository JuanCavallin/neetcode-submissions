class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[1]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        result = [0] * len(nums)
        result[0] = nums[0]
        result[1] = nums[1]
        for i in range(2, len(nums)):
            current = nums[i] + result[i - 2]
            result[i] = max(current, nums[i - 1])
        return result[-1]