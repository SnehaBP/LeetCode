class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        indexedScore = [(score[i], i) for i in range(n)]
        indexedScore.sort(reverse=True)
        result = [0] * n
        for i in range(n):
            if i == 0:
                result[indexedScore[i][1]] = "Gold Medal"
            elif i == 1:
                result[indexedScore[i][1]] = "Silver Medal"
            elif i == 2:
                result[indexedScore[i][1]] = "Bronze Medal"
            else:
                result[indexedScore[i][1]] = str(i + 1)

        return result