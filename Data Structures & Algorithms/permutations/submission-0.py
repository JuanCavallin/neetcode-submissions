from collections import defaultdict
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = [] # may not be necessary since literally only adding 
        path = []

        def backtrack():
            if len(path) == len(nums):
                result.append(path.copy())
                return
            
            for i in range(len(nums)):
                #take the combination of the remaining digits
                if nums[i] in path: #inneficient check, optimize later
                    continue
                path.append(nums[i])
                backtrack()
                path.pop()
        backtrack()
        return result
        