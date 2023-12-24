class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        reverse=[w[::-1] for w in words]
        res=' '.join(reverse)
        return res