class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        m = 1
        current = 1
        k = 1
        s = set(nums)
        visited = set()
        for val in s:
            if val in visited:
                continue
            visited.add(val)
            k = 1
            while val + k in s:
                current += 1
                k += 1
                visited.add(val + k)
            k = 1
            while v - k in s:
                current += 1
                k -= 1
                visited.add(val - k)

            m = max(m, current)
            k = 1
            current = 1
        return m

            