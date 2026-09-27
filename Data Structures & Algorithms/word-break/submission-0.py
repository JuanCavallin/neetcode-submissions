class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s in wordDict:
            return True
        for i in range(len(s)):
            if s[0:i + 1] in wordDict and self.wordBreak(s[i + 1:], wordDict):
                return True
        return False
        