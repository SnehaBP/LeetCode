class Solution:
    def checkString(self, s: str) -> bool:
        for i in range(len(s)):
            if s[i] == 'b':
                break
        if i == len(s) - 1:
            return True
        else:
            secondHalf = s[i:]
        for i in range(0, len(secondHalf)):
            if secondHalf[i] == 'a':
                return False
        return True