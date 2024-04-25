class Solution:
    def countKeyChanges(self, s: str) -> int:
        res=0
        for i in range(len(s)-1):
            if s[i+1]==s[i].upper() or s[i+1]==s[i].lower():
                continue
            else:
                print(i,s[i])
                res+=1
        return res