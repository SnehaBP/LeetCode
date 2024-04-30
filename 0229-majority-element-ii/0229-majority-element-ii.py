class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res=[]
        freqDict={}
        for num in nums:
            if num in freqDict:
                freqDict[num]+=1
            else:
                freqDict[num]=1
        for key,val in freqDict.items():
            if val>len(nums)/3:
                res.append(key)
        return res