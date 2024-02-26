class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        ans=[]
        count=0
        words=s.split()
        for word in words:
            if count<k:
                ans.append(word)
                count+=1
        return ' '.join(ans)
            