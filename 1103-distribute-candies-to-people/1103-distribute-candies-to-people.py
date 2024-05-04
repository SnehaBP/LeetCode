class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res=[0]*num_people
        n=0
        while candies>0:
            for i in range(0,num_people):
                if candies>=i+1+n:
                    res[i]+=i+1+n
                    candies-=i+1+n
                else:
                    res[i]+=candies
                    candies=0
                    break
            n+=num_people
        return res
                
                