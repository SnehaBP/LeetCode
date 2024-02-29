class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        words1Count=collections.Counter(words1)
        words2Count=collections.Counter(words2)
        count=0
        for word in set(words1+words2):
            if words1Count[word]==1 and words2Count[word]==1:
                count+=1
        return count