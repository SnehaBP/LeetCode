class Solution:
    def reformatNumber(self, number: str) -> str:
        newNum = ''.join(char for char in number if char.isdigit())
        count = len(newNum)
        reformattedNum = []

        while count > 0:
            if count > 4:
                reformattedNum.append(newNum[:3])
                newNum = newNum[3:]
                count -= 3
            elif count == 4:
                reformattedNum.append(newNum[:2])
                reformattedNum.append(newNum[2:])
                count = 0
            else: 
                reformattedNum.append(newNum[:count])
                count = 0

        return '-'.join(reformattedNum)