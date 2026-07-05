class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = nums[i] * -1
            l = i + 1
            r = len(nums) - 1
            while(l < r):
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    #how to check for duplicates in O(1)?
                    solutions.insert(-1, [nums[i], nums[l], nums[r]])
                    #
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return solutions
