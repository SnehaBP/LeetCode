class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        def countWord(s):
            wordCount={}
            words=s.split()
            for w in words:
                wordCount[w]=wordCount.get(w,0)+1
            return wordCount
        countS1=countWord(s1)
        countS2=countWord(s2)
        uncommonWords=[]
        for word , count in countS1.items():
            if count==1 and word not in countS2:
                uncommonWords.append(word)
        for word , count in countS2.items():
            if count==1 and word not in countS1:
                uncommonWords.append(word)
        return uncommonWords