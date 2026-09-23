class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = 1
        current = 1
        k = 1
        s = set(nums)
        visited = set()
        for val in s:
            if val in visited:
                continue
            visited.add(val)
            while True:
                if val + k not in s and val - k not in s:
                    break
                if val + k in s:
                    current += 1
                    visited.add(val + k)
                if val - k in s:
                    current += 1
                    visited.add(val - k)
                k += 1

            m = max(m, current)
            k = 1
            current = 1
        return m

            