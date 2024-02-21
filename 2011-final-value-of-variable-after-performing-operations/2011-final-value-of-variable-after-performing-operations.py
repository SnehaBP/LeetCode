class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res=0
        for operation in operations:
            if operation=="--X" or operation=="X--":
                res-=1
            if operation=="++X" or operation=="X++":
                res+=1
        return res