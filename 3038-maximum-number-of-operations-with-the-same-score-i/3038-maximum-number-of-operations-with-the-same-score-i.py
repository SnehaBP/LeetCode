class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        count=0
        sumOfTowNums=nums[0]+nums[1]
        for i in range(0,len(nums)-1,2):
            if (nums[i]+nums[i+1])==sumOfTowNums:
                print(nums[i]+nums[i+1])
                count+=1
            else:
                break
        return count
                