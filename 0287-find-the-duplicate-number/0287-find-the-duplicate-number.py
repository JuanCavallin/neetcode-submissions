class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = 0
        fast = 0
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                # Found loop, now increment both by 1 or something
                slow = 0
                while slow != fast:
                    slow = nums[slow]
                    fast = nums[fast]
                return slow

        return -1
