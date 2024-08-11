class Solution:
    def replaceDigits(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            if i % 2 == 0:
                res = res + s[i]
            else:
                ch = ord(s[i-1]) + int(s[i])
                res = res + chr(ch)
        return res