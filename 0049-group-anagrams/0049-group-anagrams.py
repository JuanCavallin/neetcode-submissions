class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = defaultdict(list)
        a = ord('a')
        for word in strs:
            key = [0] * 26
            for c in word:
                idx = ord(c) - a
                key[idx] += 1
            d[tuple(key)].append(word)

        return list(d.values())