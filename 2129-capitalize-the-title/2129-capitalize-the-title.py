class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words=title.split()
        lst=[]
        for word in words:
            if len(word)<=2:
                lst.append(word.lower() + " ")
            else:
                lst.append(word[0].upper() + word[1:].lower() + " ")
        return "".join(lst).rstrip()