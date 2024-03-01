class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        subarrays=[(nums[i],nums[i+1]) for i in range(len(nums)-1)]  
        sumofSubarray=[]
        sumSet=set()
        for subarray in subarrays:
            sumofSubarray.append(sum(subarray))
        for sumValue in sumofSubarray:
            if not sumValue in sumSet:
                sumSet.add(sumValue)
            else:
                return True
        return False