class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        content=0
        gIndex=0
        sIndex=0
        while gIndex<len(g) and sIndex<len(s):
            if s[sIndex]>=g[gIndex]:
                content+=1
                gIndex+=1
            sIndex+=1
        return content
        