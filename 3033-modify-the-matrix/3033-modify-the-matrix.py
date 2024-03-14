class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        numRows=len(matrix)
        numCols=len(matrix[0])
        for j in range(numCols):
            maxEle=0
            for i in range(numRows):
                maxEle=max(maxEle,matrix[i][j])
            for i in range(numRows):
                if matrix[i][j]==-1:
                        matrix[i][j]=maxEle
        return matrix