class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        res = 0
        upperPrev = 0
        for upper, percent in brackets:
            if income > upper:
                res += (upper - upperPrev) * (percent / 100)
                upperPrev = upper
            else:
                res += (income - upperPrev) * (percent / 100)
                break
        return res