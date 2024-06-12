class Solution:
    def clearDigits(self, s: str) -> str:
        s = list(s)
        i = 0
        while i < len(s):
            if s[i].isdigit():
                if i > 0:
                    s.pop(i)
                    s.pop(i-1)
                    i -= 1
                else:
                    s.pop(i) 
            else:
                i += 1
        return "".join(s)