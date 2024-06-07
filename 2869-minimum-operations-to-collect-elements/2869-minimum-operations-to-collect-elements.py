class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        numsRemoved = []
        for i in range(len(nums)-1 , -1, -1):
            numsRemoved.append(nums[i])
            flag = 0
            for j in range(1 , k+1):
                if j not in numsRemoved:
                    flag = 0
                    break
                else:
                    flag = 1
            if flag == 1:
                return len(numsRemoved)