class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        lst=set()
        for n in nums:
            if n in lst:
                return True
            else:
                lst.add(n)
        return False