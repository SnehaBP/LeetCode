class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        count = 0
        j = -1
        while count <= k+1:
            for i in range(j+1, n):
                count +=1
                if count == k+1:
                    return i 
            for j in range(n-2, -1, -1):
                count +=1
                if count == k+1:
                    return j