class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = defaultdict(list)
        for word in strs:
            key = [0] * 26
            for c in word:
                idx = ord(c) - ord('a')
                key[idx] += 1
            d[str(key)].append(word)

        return list(d.values())