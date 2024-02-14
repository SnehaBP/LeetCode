class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n=len(arr)
        toTrim=int(n*0.05)
        trimedArr=arr[toTrim:n-toTrim]
        return sum(trimedArr)/len(trimedArr)