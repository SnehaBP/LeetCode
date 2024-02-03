class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def customKey(num):
            return bin(num).count('1'),num
        sortedArr=sorted(arr,key=customKey)
        return sortedArr