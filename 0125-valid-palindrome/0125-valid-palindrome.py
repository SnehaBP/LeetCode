class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=""
        for c in s.lower():
            if c.isalnum():
                st+=c
        return st == st[::-1]