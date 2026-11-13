class Solution:
    def minOperations(self, n: int) -> int:
        current = n
        largest = 1
        result = 0
        while largest < n:
            largest *= 2
        while current != 0:
            a = abs(current - largest)
            b = abs(current - max(largest // 2, 1))
            current = min(a, b)
            while largest // 2 > current:
                largest //= 2            
            result += 1

        return result