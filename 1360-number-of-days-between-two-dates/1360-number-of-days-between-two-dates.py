class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        dateObj1=date(*map(int,date1.split('-'))) 
        dateObj2=date(*map(int,date2.split('-'))) 
        diff=abs((dateObj1-dateObj2).days)
        return diff