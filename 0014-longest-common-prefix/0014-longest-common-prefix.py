class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        commonPrefix=[]
        strs.sort()
        fStr=strs[0]
        lStr=strs[-1]
        for s in range(len(fStr)):
            if s<len(lStr) and fStr[s]==lStr[s]:
                commonPrefix.append(fStr[s])
            else:
                break
        return "".join(commonPrefix)