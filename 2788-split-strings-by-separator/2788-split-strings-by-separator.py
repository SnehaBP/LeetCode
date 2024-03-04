class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res=[]
        for word in words:
            res.append(word.split(separator))
        return [string for string in sum(res,[]) if string!=""]