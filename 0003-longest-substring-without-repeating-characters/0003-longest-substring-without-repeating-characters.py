class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        l, r = 0, 0
        freq = defaultdict(int)
        while r < len(s):
            freq[s[r]] += 1
            if freq[s[r]] > 1:
                result = max(result, r - l)
                while l < r and freq[s[r]] > 1:
                    freq[s[l]] -= 1
                    l += 1


            r += 1
        
        return max(result, r - l)