class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        l =len(grid)
        res = []
        flattenedList = [item for sublist in grid for item in sublist]
        counter = collections.Counter(flattenedList)
        for val, count in counter.items():
            if count == 2:
                res.append(val)
        for i in range(1, l * l + 1):
            if i not in flattenedList:
                res.append(i)
                break
        return res
            