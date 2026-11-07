class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        maxQueue = deque()
        minQueue = deque()
        l, r = 0, 0
        result = 0
        while r < len(nums):
            k = nums[r]
            while maxQueue and k > maxQueue[-1]:
                maxQueue.pop()
            maxQueue.append(k)
            while minQueue and k < minQueue[-1]:
                minQueue.pop()
            minQueue.append(k)
            r += 1
            
            while maxQueue[0] - minQueue[0] > limit:
                if maxQueue and maxQueue[0] == nums[l]:
                    maxQueue.popleft()
                if minQueue and minQueue[0] == nums[l]:
                    minQueue.popleft()
                l += 1
            result = max(result, r - l)
        return result
                