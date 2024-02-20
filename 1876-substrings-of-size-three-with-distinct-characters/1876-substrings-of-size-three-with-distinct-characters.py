class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count=0
        for i in range(len(s)-2):
            substr=s[i:i+3]
            seen=set()
            isGood=True
            for char in substr:
                if char in seen:
                    isGood=False
                    break 
                seen.add(char)
            if isGood:
                count+=1
        return count
                
                