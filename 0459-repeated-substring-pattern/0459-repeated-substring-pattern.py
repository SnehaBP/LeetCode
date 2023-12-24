class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1,len(s)//2+1):
            if len(s)%i==0:
                subStr=s[:i]
                repeated=len(s)//i
                if subStr*repeated==s:
                    return True
        return False