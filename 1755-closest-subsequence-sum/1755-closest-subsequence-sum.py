class Solution:
    def minAbsDifference(self, nums: list[int], goal: int) -> int:
        result = float('inf')
        #prev = SortedList([0])

        def getPrefixSums(arr):
            prefix = [0]
            for n in arr:
                newSums = []
                for x in prefix:
                    newSums.append(x + n)
                prefix.extend(newSums)
            prefix.sort()
            return prefix

        left = getPrefixSums(nums[0:len(nums) // 2])
        right = getPrefixSums(nums[len(nums) // 2:])
        l, r = 0, len(right) - 1
        while l < len(left) and r >= 0:
            total = right[r] + left[l]

            result = min(result, abs(total - goal))
            if result == 0:
                return 0
            
            if total > goal:
                r -= 1
            else:
                l += 1

        return result