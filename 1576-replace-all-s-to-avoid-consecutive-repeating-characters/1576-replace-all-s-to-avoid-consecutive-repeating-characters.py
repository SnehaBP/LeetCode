class Solution:
    def modifyString(self, s: str) -> str:
        s=list(s)
        for i in range(len(s)):
            if s[i]=="?":
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if i==0 and (i==len(s)-1 or c!=s[i+1]):
                        s[i]=c
                        break
                    elif i==len(s)-1 and c!=s[i-1]:
                        s[i]=c
                        break
                    elif c!=s[i-1] and c!=s[i+1]:
                        s[i]=c
                        break
        return "".join(s)