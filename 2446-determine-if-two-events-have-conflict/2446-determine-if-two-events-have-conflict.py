class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        startTime1,endTime1=event1
        startTime2,endTime2=event2
        startTime1InMin=int(startTime1[:2]*60)+int(startTime1[3:])
        startTime2InMin=int(startTime2[:2]*60)+int(startTime2[3:])
        endTime1InMin=int(endTime1[:2]*60)+int(endTime1[3:])
        endTime2InMin=int(endTime2[:2]*60)+int(endTime2[3:])
        if startTime2InMin<=endTime1InMin and endTime2InMin>=startTime1InMin:
            return True
        return False