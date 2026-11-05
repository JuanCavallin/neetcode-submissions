class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        result = [0] * (n + 1)
        for start, last, seats in bookings:
            result[start] += seats
            if last < n:
                result[last + 1] -= seats
        
        print(result)
        current = 0
        for i in range(1, n + 1):
            print("Current", current)
            current += result[i]
            result[i] = current

        # ??? How to first compute the total for each range (1-2 have 40 flights each)
        return result[1:]