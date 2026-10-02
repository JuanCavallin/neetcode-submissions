class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        current = 0
        jumps = 0
        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
            if farthest >= len(nums) - 1:
                return True
            if i == current:
                current = farthest
                jumps += 1

        return False