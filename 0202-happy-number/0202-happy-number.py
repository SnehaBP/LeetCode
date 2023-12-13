class Solution:
    def isHappy(self, n: int) -> bool:
        max_iterations=100
        def nextSquare(num):
            sum=0
            for digit in str(num):
                sum+=int(digit)**2
            return sum
        for _ in range(max_iterations):
            n=nextSquare(n)
            if n==1:
                return True
        return False