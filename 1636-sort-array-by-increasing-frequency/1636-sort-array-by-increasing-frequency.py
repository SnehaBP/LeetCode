class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freqDict={}
        for i in nums:
            if i in freqDict:
                freqDict[i]+=1
            else:
                freqDict[i]=1
        def custemKey(x):
            return (freqDict[x],-x)
        sortedList=sorted(nums,key=custemKey)
        return sortedList