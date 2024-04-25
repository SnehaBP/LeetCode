class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count=0
        for ch in word:
            if ch.islower():
                if ch.upper() in word:
                    word=word.replace(ch.upper(), '/')
                    count+=1
        return count