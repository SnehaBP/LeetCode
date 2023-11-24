class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk = []
        dic = {'(': ')', '[': ']', '{': '}'}
        for ch in s:
            if stk and stk[-1] in "([{" and dic[stk[-1]] == ch:
                stk.pop()
            else:
                stk.append(ch)
        return not stk