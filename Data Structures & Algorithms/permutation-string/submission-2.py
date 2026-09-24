class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # str1 = "abc"
        # str2 = "acab"
        #
        if len(s2) < len(s1):
            return False

        l = 0
        r = 0
        
        # Populate the matching t
        #  TODO: after make it skip certain elements by iterating while not equal to i
        frequencies1 = [0] * 26
        for c in s1:
            idx = ord(c) - ord('a')
            frequencies1[idx] += 1

        # Build sliding window with first ele
        frequencies2 = [0] * 26
        #for i in range(r + 1):
        #    idx = ord(s2[i]) - ord('a')
        #    frequencies2[idx] += 1

        # Move window and check
        while r < len(s2):    
            if frequencies2 == frequencies1:
                return True
            print(frequencies2)
            print("r:", r, "l:", l)
            c = ord(s2[r]) - ord('a')
            frequencies2[c] += 1
            r += 1
            if r - l > len(s1):   
                prev = ord(s2[l]) - ord('a')
                frequencies2[prev] -= 1
                l += 1
        
        return False

        
