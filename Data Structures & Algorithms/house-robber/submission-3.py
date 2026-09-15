class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        result = [0] * len(nums)
        result[0] = nums[0]
        result[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            current = nums[i] + result[i - 2]
            result[i] = max(current, result[i - 1])
        return result[-1]