class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        length=len(s)
        seen=set()
        repeated=set()
        if length<10:
            return 
        for i in range(length-9):
            seq=s[i:i+10]
            if seq in seen:
                repeated.add(seq)
            else:
                seen.add(seq)
        return list(repeated)