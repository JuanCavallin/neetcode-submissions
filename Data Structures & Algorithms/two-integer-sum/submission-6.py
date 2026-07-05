class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        reverse = dict()
        for i in range(len(nums)):
            num = nums[i]
            if (target - num) in reverse:
                return [reverse[target - num], i]
            reverse[num] = i;