class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        l = min(bloomDay)
        r = max(bloomDay)
        while l <= r:
            bouquets = 0
            current = 0
            day = (l + r) // 2
            for bloom in bloomDay:
                if bloom <= day:
                    current += 1
                else:
                    current = 0

                if current == k:
                    bouquets += 1
                    current = 0

                if bouquets == m:
                    break
            if bouquets == m:
                r = day - 1
            else:
                l = day + 1

        return l
 
        