class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters =set()
        for i in sentence:
            if i not in letters:
                letters.add(i)
            if len(letters) == 26:
                return True
        return False