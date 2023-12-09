class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        w1 = len(word1)-1
        w2 = len(word2)-1
        l = min(w1, w2)
        for i in range(l+1):
            merged += word1[i] + word2[i]
        if w1 == w2:
            return merged
        elif w1 > w2:
            return merged + word1[l+1:]
        elif w1 < w2:
            return merged + word2[l+1:]