class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        l, r = 0, 0
        freq = set()
        while r < len(s):
            if(s[r] in freq):
                k = s[r]
                result = max(result, r - l)
                while l < r and s[r] in freq:
                    freq.remove(s[l])
                    l += 1

            freq.add(s[r])
            r += 1
        
        return max(result, r - l)