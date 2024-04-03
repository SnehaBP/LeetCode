class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowHavingZero=set()
        colHavingZero=set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    rowHavingZero.add(i)
                    colHavingZero.add(j)
        for row in rowHavingZero:
            for i in range(len(matrix[0])):
                matrix[row][i]=0
        for col in colHavingZero:
            for i in range(len(matrix)):
                matrix[i][col]=0