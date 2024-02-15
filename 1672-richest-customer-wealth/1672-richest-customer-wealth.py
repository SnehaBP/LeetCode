class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res=[]
        for row in accounts:
            sum=0
            for element in row:
                sum=sum+element
                res.append(sum)
        return max(res)