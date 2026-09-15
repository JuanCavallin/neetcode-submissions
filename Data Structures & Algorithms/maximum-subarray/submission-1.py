class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = [0] * len(nums)
        result[0] = nums[0]
        for i in range(1, len(nums)):
            result[i] = max(result[i -1] + nums[i], nums[i])
            print(result[i])

        return result[-1]