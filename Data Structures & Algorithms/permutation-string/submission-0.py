class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # str1 = "abc"
        # str2 = "acab"
        #
        if len(s2) < len(s1):
            return False

        l = 0
        r = len(s1) - 1
        
        # Populate the matching t
        #  TODO: after make it skip certain elements by iterating while not equal to i
        frequencies1 = [0] * 26
        for c in s1:
            idx = ord(c) - ord('a')
            frequencies1[idx] += 1


        frequencies2 = [0] * 26
        for i in range(r):
            if frequencies2 == frequencies1:
                return True

            idx = ord(s2[i]) - 'a'
            frequencies2[idx] += 1
        while r < len(s2):    
            c = s2[r]
            if frequencies1[c] > 0:
                frequencies2[c] += 1
            r += 1
            prev = s2[l]
            frequencies2[l] -= 1
            l += 1
        
        return False

        
