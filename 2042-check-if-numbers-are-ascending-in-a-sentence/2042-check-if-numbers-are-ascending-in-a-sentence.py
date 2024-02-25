class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        words=s.split()
        listOfNums=[]
        for word in words:
            if word.isdigit():
                listOfNums.append(int(word))
        for i in range(len(listOfNums)-1):
            if listOfNums[i]>=listOfNums[i+1]:
                return False
                break
        return True