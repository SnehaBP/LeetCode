class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def sortingKey(row):
            return (rowStrenght[row],row)
        rowStrenght={i:sum(row) for i,row in zip(range(len(mat)),mat)}
        sortedRows=sorted(rowStrenght,key=sortingKey)
        return sortedRows[:k]