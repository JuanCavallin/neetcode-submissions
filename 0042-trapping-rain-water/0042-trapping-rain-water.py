class Solution:
    def trap(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        maxLeft = height[0]
        maxRight = height[len(height) - 1]
        result = 0
        while l <= r:
            
            if maxLeft < maxRight:
                result += max(0, maxLeft - height[l])
                maxLeft = max(maxLeft, height[l])
                l += 1
            else:
                result += max(0, maxRight - height[r])
                maxRight = max(maxRight, height[r])
                r -= 1                
        
        return result

