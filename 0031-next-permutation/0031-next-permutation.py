class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        minIdx = len(nums) - 1
        minNum = float('inf')
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                for j in range(len(nums) - 1, i - 1, -1):
                    if nums[j] > nums[i - 1]:
                        nums[i - 1], nums[j] = nums[j], nums[i - 1]
                        break
                nums[i:] = nums[i:][::-1]
                return
        nums.reverse()

                

        