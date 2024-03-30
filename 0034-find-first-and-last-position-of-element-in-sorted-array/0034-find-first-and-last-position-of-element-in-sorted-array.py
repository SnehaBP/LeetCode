class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res=[]
        flag1=0
        flag2=0
        for i in range(0,len(nums),1):
            if nums[i]==target:
                res.append(i)
                flag1=1
                break
        if flag1==0:
            res.append(-1)
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==target:
                res.append(i)
                flag2=1
                break
        if flag2==0:
            res.append(-1)
        return res
        