class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        res=[]
        for ele in nums:
            ele=str(ele)
            if len(ele)>1:
                maxDig=ele[0]
                for i in range(1,len(ele)):
                    if ele[i]>maxDig:
                        maxDig=ele[i]
                encryptedNum=""
                for j in range(len(ele)):
                    encryptedNum=encryptedNum+str(maxDig)
                res.append(int(encryptedNum))
            else:
                res.append(int(ele))
        print(res)
        return sum(res)                    