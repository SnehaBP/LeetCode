class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        rs5=0
        rs10=0
        for bill in bills:
            if bill == 5:
                rs5+=1
            elif bill == 10:
                rs10+=1
                if rs5>0:
                    rs5-=1
                else:
                    return False
            elif bill == 20:
                if rs5>0 and rs10>0:
                    rs10-=1
                    rs5-=1
                elif rs5>=3:
                    rs5-=3
                else:
                    return False
        return True
            
            
            