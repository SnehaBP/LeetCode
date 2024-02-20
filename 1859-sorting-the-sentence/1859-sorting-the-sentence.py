class Solution:
    def sortSentence(self, s: str) -> str:
        lst=['']*10
        words=s.split()
        for word in words:
            position=int(word[-1])
            lst[position]=word[:-1]
        return " ".join(lst[1:]).rstrip()
            