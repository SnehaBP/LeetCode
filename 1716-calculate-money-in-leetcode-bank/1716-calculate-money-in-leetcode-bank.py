class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        def trapezoid(a, b):
            return (a + b) * (b - a + 1) // 2

        weeks = n // 7
        firstWeek = trapezoid(1, 7)
        lastFullWeek = trapezoid(1 + weeks - 1, 7 + weeks - 1)
        remainingDays = trapezoid(1 + weeks, n % 7 + weeks)
        return (firstWeek + lastFullWeek) * weeks // 2 + remainingDays
        