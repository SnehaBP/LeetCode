class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        duration = []
        duration.append(logs[0][1] - 0)
        for i in range(1, len(logs)): 
            duration.append(logs[i][1] - logs[i-1][1])
        maxDuration = max(duration)
        maxDurationIndexes = [i for i, d in enumerate(duration) if d == maxDuration]
        hardestWorker = min(logs[i][0] for i in maxDurationIndexes) 
        return hardestWorker