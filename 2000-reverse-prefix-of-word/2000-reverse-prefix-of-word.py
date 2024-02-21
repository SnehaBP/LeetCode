class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        prefix=""
        for i in range(len(word)):
            if word[i]==ch:
                prefix=word[0:i+1]
                break
        return prefix[::-1]+word[i+1:len(word)+1]