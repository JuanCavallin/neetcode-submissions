class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        types = 0
        result = 0
        freq = defaultdict(int)
        l, r = 0, 0
        while r < len(fruits):
            freq[fruits[r]] += 1
            if freq[fruits[r]] == 1:
                types += 1
            r += 1
            while types > 2:
                freq[fruits[l]] -= 1
                if freq[fruits[l]] == 0:
                    types -= 1
                l += 1
            result = max(result, r - l)


        return result