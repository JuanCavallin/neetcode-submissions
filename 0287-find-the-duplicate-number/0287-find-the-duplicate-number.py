class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]

            if slow == fast:
                slow = 0
                while nums[slow] != nums[fast]:
                    slow = nums[slow]
                    fast = nums[fast]
                return nums[fast]
            
        