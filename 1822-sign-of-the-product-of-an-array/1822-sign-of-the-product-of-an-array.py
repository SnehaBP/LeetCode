class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        else:
            Ncount = 0
            for n in nums:
                if n < 1:
                    Ncount += 1
            print(Ncount)
            if Ncount % 2 == 0:
                return 1
            if Ncount % 2 !=0:
                return -1