class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        concatinatedWords=''
        for word in words:
            concatinatedWords=concatinatedWords+word
            if concatinatedWords==s:
                break
        return concatinatedWords==s