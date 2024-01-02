class Solution:
    def checkRecord(self, s: str) -> bool:
        absences = 0
        consecutiveLate = 0
        for c in s:
            if c == 'A':
                absences += 1
                consecutiveLate = 0
            elif c == 'L':
                consecutiveLate += 1
            else:
                consecutiveLate = 0  
            if absences >= 2 or consecutiveLate >= 3:
                return False
        return True