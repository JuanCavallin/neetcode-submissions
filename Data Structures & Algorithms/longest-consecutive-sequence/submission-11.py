class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = 0
        current = 1
        s = set(nums)
        for val in s:
            if val - 1 in s:
                continue
            while val + current in s:
                current += 1
            m = max(m, current)
            current = 1
            
        return m

            