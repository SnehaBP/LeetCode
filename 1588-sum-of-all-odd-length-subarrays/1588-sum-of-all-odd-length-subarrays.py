class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res=set()
        totalSum=0
        for length in range(1, len(arr)+1, 2):
            for start in range(len(arr) - length + 1):
                end = start + length
                totalSum += sum(arr[start:end])
        return totalSum