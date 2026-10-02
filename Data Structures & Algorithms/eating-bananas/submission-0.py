class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles:
            return 0
        l = 1
        r = sum(piles)
        def canFinish(k):
            n = 0
            for i in range(len(piles)):
                n += (piles[i] + k - 1) // k
                if n > h:
                    return False
            return True

        while l < r:
            mid = (l + r) // 2
            # Try to see if you can eat all the bananas before 9 hours in 
            if canFinish(mid):
                r = mid
            else:
                l = mid + 1
        
        return l