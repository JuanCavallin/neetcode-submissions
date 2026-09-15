class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            if i == 0:
                longest = s[0]
            l, r = i - 1, i + 1
            while(r < len(s) and s[r] == s[i]):
                r += 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            l += 1
            ns = s[l:r]
            if len(ns) > len(longest):
                longest = ns
        return longest