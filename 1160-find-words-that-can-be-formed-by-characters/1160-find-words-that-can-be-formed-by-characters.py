class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        charsCounter = collections.Counter(chars)
        for word in words:
            flag = 0
            wordCounter = collections.Counter(word)
            for letter in word:
                if letter not in chars or wordCounter[letter] > charsCounter[letter]:
                    flag = 1
                    break
            if flag == 0:
                count += len(word)
        return count