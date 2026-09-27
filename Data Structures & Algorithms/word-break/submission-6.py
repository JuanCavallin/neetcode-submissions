class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        visited = set()
        def helper(s):
            if s in wordDict:
                return True
            if s in visited:
                return False
            for i in range(len(s)):
                if s[0:i + 1] in wordDict:
                    if self.wordBreak(s[i + 1:], wordDict):
                        return True
            visited.add(s)
            return False
        return helper(s)
        