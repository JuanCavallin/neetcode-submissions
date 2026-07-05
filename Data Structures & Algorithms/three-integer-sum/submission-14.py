from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solutions = []
        n = len(nums)

        for i in range(n - 2):
            # skip duplicate anchors
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # optional early stop: if nums[i] > 0, remaining are >= nums[i]
            if nums[i] > 0:
                break

            target = -nums[i]
            l, r = i + 1, n - 1

            while l < r:
                s = nums[l] + nums[r]
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    # found a unique triplet (because we skipped dup i, and will skip dup l/r)
                    solutions.append([nums[i], nums[l], nums[r]])

                    l += 1
                    r -= 1

                    # skip duplicates for l and r so we don't add the same triplet again
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return solutions
