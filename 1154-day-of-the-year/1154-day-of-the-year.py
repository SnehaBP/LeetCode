class Solution:
    def dayOfYear(self, date: str) -> int:
        monthDict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        year = int(date[0:4])
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            monthDict[2] = 29
        month = int(date[5:7])
        day = int(date[8:10])
        res = day
        for i in range(1, month):
            res += monthDict[i]
        return res
            