class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1=set("qwertyuiopQWERTYUIOP")
        row2=set("asdfghjklASDFGHJKL")
        row3=set("zxcvbnmZXCVBNM")
        res=[]
        for w in words:
            if w[0] in row1:
                row=row1
            elif w[0] in row2:
                row=row2
            elif w[0] in row3:
                row=row3
            if all(char in row for char in w):
                res.append(w)
        return res