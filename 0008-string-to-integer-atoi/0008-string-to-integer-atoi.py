class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        idx = 0
        negative = False
        result = 0

        if s[0] == '+' or s[0] == '-':
            idx += 1
            if s[0] == '-':
                negative = True
        #skip leading 0s
        while idx < len(s) and s[idx] == 0:
            idx += 1


        for i in range(idx, len(s)):
            digit = (ord(s[i]) - ord('0'))
            if 0 <= digit <= 9:
                result = result * 10 + digit
            else:
                break
        if negative:
            return -(min(result, 2147483648))
        return min(result, 2147483647)
