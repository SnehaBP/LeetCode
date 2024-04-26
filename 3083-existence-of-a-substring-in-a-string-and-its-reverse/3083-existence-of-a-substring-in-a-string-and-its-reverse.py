class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        reverseds=s[::-1]
        for i in range(len(s)-1):
            sOfLen2=s[i]+s[i+1]
            if sOfLen2 in reverseds:
                return True
        return False