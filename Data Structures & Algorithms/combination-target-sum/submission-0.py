class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #This is basically the same as getting all the set values but I return early on path that matches or excedes target
        path = []
        result = []

        def backtrack(current, sum):
            if sum == target:
                result.append(path.copy())
                return
            for i in range(current, len(nums)):
                if sum + nums[i] > target:
                    continue #do not add more stuff, increment i by 1
                path.append(nums[i])
                backtrack(i, sum + nums[i])
                path.pop()

        backtrack(0, 0)

        return result