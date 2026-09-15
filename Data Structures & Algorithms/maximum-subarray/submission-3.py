class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        num1 = nums[0]
        nums2 = 0
        current_max = nums[0]
        for i in range(1, len(nums)):
            nums2 = max(num1 + nums[i], nums[i])
            if current_max < nums2:
                current_max = nums2
            nums1 - nums2
        return current_max