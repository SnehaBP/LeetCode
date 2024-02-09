class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        minRow=[min(row) for row in matrix]
        transMatrix=[]
        for i in range(len(matrix[0])):
            columns=[matrix[j][i] for j in range(len(matrix))]
            transMatrix.append(columns)
        maxCol=[max(col) for col in transMatrix]
        luckyNo=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==minRow[i] and matrix[i][j]==maxCol[j]:
                    luckyNo.append(matrix[i][j])
        return luckyNo