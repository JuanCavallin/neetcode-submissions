from collections import deque

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        result = 0
        l, r = 0, 0
        minimums = deque() # minmimum at position 0 
        maximums = deque() # max a t position 0

        while r < len(nums):
            while minimums and nums[r] < nums[minimums[-1]]:
                minimums.pop()
            minimums.append(r)

            while maximums and nums[r] > nums[maximums[-1]]:
                maximums.pop()
            maximums.append(r)
            while l < r and abs(nums[minimums[0]] - nums[maximums[0]]) > 2:
                if l == minimums[0]:
                    minimums.popleft()
                if l == maximums[0]:
                    maximums.popleft()
                l += 1 

            mini, maxi = nums[minimums[0]], nums[maximums[0]]
            if abs(mini - maxi) <= 2:
                result += (r - l + 1)

            r += 1
        
        return result