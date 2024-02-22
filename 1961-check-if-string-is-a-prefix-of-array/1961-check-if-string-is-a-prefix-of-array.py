class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        flag=0
        concatinatedWords=''
        for word in words:
            concatinatedWords=concatinatedWords+word
            if concatinatedWords==s:
                flag=1
                break
        return flag==1