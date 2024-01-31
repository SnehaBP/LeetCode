class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        totalTime = 0
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]

            horizontalDist = abs(x2 - x1)
            verticalDist = abs(y2 - y1)
            diagonalDist = max(horizontalDist, verticalDist)

            totalTime += diagonalDist

        return totalTime