class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letterLst = []
        res = []
        for l in s:
            if l.isalpha():
                letterLst.append(l)
        letterLst.reverse()
        letterIndex = 0
        for l in s:
            if l.isalpha():
                res.append(letterLst[letterIndex])
                letterIndex += 1
            else:
                res.append(l)
        return "".join(res)