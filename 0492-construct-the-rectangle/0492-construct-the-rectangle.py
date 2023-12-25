class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        sqrt=isqrt(area)
        for length in range(sqrt,0,-1):
            if area%length==0:
                width=area//length
                return [max(length,width),min(length,width)]