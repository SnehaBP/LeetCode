class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        greaterLetters = [l for l in letters if l > target]
        sortedLetters = sorted(greaterLetters)
        if not sortedLetters:
            return letters[0]
        return sortedLetters[0]