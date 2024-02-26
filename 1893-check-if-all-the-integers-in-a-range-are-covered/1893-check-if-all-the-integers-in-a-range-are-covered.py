class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        numRange = [False] * (right - left + 1) 
        for start, end in ranges:
            for num in range(start, end + 1):
                if left <= num <= right:  
                    numRange[num - left] = True  
        return all(numRange)
