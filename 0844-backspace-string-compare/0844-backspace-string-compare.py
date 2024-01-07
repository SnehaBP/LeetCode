class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def processString(string):
            res=[]
            for c in string:
                if c=="#":
                    if res:
                        res.pop()
                else:
                    res.append(c)
            return res
        return processString(s)==processString(t)