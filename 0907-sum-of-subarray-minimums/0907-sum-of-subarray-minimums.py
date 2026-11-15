from collections import deque

class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        stack = [] # minimum, how many subarrays match that value
        current = 0
        result = 0 
        for num in arr:
            count = 1
            while stack and stack[-1][0] >= num: # check how many new subarrays have this as the minimum
                current -= stack[-1][0] * stack[-1][1]
                count += stack[-1][1]
                stack.pop()
                
            current += count * num
            result += current
            stack.append((num, count))
        
        return result % (pow(10, 9) + 7)