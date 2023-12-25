class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        poisonedTime=0
        for i in range(1,len(timeSeries)):
            time=min(duration,timeSeries[i]-timeSeries[i-1])
            poisonedTime+=time
        poisonedTime+=duration
        return poisonedTime