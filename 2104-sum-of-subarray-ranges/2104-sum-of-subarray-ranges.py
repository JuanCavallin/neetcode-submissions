from collections import deque

class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        current_min, current_max = 0, 0
        result = 0
        minimums, maximums = deque(), deque()

        for num in nums:
            freq_min, freq_max = 1, 1
            while minimums and num <= minimums[-1][0]:
                freq_min += minimums[-1][1]
                current_min -= minimums[-1][0] * minimums[-1][1]
                minimums.pop()
            current_min += freq_min * num
            minimums.append((num, freq_min))

            while maximums and num >= maximums[-1][0]:
                freq_max += maximums[-1][1]
                current_max -= maximums[-1][0] * maximums[-1][1]
                maximums.pop()
            maximums.append((num, freq_max))
            current_max += freq_max * num
        
            result += current_max - current_min
        
        return result
