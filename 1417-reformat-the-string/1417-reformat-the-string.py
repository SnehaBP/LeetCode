class Solution:
    def reformat(self, s: str) -> str:
        if s.isalpha() and len(s)>1:
            return ""
        if s.isdigit() and len(s)>1:
            return ""
        if s.isalpha() and len(s)==1:
            return s
        if s.isdigit() and len(s)==1:
            return s
        else:
            res=''
            alpha=''.join(filter(str.isalpha,s))
            dig=''.join(filter(str.isdigit,s))
            minLen=min(len(alpha),len(dig))
            if len(dig)>=len(alpha)+2 or len(alpha)>=len(dig)+2:
                return ""
            if len(dig)>=len(alpha):
                for i in range(minLen):
                    res+=dig[i]+alpha[i]
                res+=dig[minLen:]+alpha[minLen:]
            if len(alpha)>len(dig):
                for i in range(minLen):
                    res+=alpha[i]+dig[i]
                res+=alpha[minLen:]+dig[minLen:]
            return res