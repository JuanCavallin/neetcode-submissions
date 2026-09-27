class Solution:
    visited = set()
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s in wordDict:
            return True
        if s in self.visited:
            return False
        for i in range(len(s)):
            if s[0:i + 1] in wordDict:
                if self.wordBreak(s[i + 1:], wordDict):
                    return True
                self.visited.add(s[i + 1:])
        return False
        