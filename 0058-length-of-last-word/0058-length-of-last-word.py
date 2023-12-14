class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words=s.split()
        if not words:
            return 0
        else:
            return len(words[-1])
        