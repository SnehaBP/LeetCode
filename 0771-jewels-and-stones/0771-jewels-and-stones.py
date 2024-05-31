class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stonesList=[]
        count=0
        for k in stones:
            stonesList.append(k)
        for i in jewels:
            for j in stonesList:
                if i == j:
                    count+=1
        return count