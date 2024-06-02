class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res = []
        minDiff = float('inf')
        for i in range(len(arr)-1):
            minDiff = min(minDiff , abs(arr[i] - arr[i+1]))
        for i in range(len(arr)-1):
            if minDiff == abs(arr[i] - arr[i+1]):
                res.append([arr[i] , arr[i+1]])
        return res
                