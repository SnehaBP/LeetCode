class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freqDict = {}
        res = []
        for a in arr:
            if a in freqDict:
                freqDict[a] += 1
            else:
                freqDict[a] = 1
        for val , key in freqDict.items():
            if key == 1:
                res.append(val)
        if k <= len(res):
            return res[k-1]
        return ''
            