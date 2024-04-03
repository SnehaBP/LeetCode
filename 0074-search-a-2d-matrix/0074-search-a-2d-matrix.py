class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flag=0
        for row in matrix:
            for ele in row:
                if ele==target:
                    flag=1
        return flag