class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        ans=0
        for x1, y1 in points:
            for x2, y2 in points:
                for x3, y3 in points:
                    ans = max(ans, 0.5 * abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)))

        return ans
        