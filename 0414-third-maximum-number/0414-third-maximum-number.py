class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        uniqueItems = list(set(nums))
        if len(uniqueItems)<3:
            return max(nums)
        firstMaxNo=max(uniqueItems)
        uniqueItems.remove(firstMaxNo)
        secMaxNo=max(uniqueItems)
        uniqueItems.remove(secMaxNo)
        return max(uniqueItems)