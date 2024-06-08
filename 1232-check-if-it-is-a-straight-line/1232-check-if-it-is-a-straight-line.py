class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        if n == 2:
            return True
        (x1, y1), (x2, y2) = coordinates[0], coordinates[1]
        dx = x2 - x1
        dy = y2 - y1
        for i in range(2, len(coordinates)):
            x, y =coordinates[i]
            if dx* (y1 - y) != dy* (x1 - x):
                return False
        return True
        