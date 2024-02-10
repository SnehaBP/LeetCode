class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res=[]
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[j] in words[i]:
                    res.append(words[j])
                if words[i] in words[j]:
                    res.append(words[i])
        return list(set(res))