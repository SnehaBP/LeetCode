class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        minDiff = -1
        for i in range(len(s)):
            for j in range(len(s)-1, i, -1):
                if s[i] == s[j]:
                    minDiff = max(minDiff , j-i-1)
                    break
        return minDiff
            