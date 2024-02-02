class Solution:
    def maximum69Number (self, num: int) -> int:
        numString=str(num)
        for i in range(len(numString)):
            if numString[i]=="6":
                return int(numString[:i]+'9'+numString[i+1:])
        return num
            