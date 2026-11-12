class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        result = [pref[0]]
        for i in range(1, len(pref)):
            result.append(pref[i] ^ pref[i - 1])
        return result