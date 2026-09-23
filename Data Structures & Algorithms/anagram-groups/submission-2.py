from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)
        for s in strs:
            arr = [0] * 26
            for c in s:
                idx = ord(c) - ord('a')
                arr[idx] += 1
            t = tuple(arr)
            dictionary[t].append(s)
        return list(dictionary.values())



