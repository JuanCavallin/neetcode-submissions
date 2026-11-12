class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        result = 0
        while l < r:
            temp = min(height[r], height[l]) * (r - l)
            result = max(result, temp)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return result