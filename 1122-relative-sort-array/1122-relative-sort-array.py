class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count1=collections.Counter(arr1)
        res=[]
        for a in arr2:
            if a in count1:
                res.extend([a] * count1[a])
                del count1[a]
        for key in sorted(count1.keys()):
            res.extend([key] * count1[key])
        return res
        