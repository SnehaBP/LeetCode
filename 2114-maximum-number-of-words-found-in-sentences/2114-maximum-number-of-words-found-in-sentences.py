class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count=0
        for sentence in sentences:
            words=sentence.split()
            if len(words)>count:
                count=len(words)
        return count