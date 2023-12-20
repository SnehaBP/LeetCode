class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineCount={}
        for m in magazine:
            if m in magazineCount:
                magazineCount[m]+=1
            else:
                magazineCount[m]=1
        for r in ransomNote:
            if r not in magazineCount or magazineCount[r]==0:
                return False
            magazineCount[r]-=1
        return True