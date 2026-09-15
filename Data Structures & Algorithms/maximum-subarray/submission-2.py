class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = [0] * len(nums)
        result[0] = nums[0]
        current_max = nums[0]
        for i in range(1, len(nums)):
            result[i] = max(result[i -1] + nums[i], nums[i])
            if current_max < result[i]:
                current_max = result[i]
            print(result[i])

        return current_max