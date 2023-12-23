class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=set("aeiouAEIOU")
        s=list(s)
        start,end=0,len(s)-1
        while end>start:
            while end>start and s[start].lower() not in vowels:
                start+=1
            while end>start and s[end].lower() not in vowels: 
                end-=1
            s[start],s[end]=s[end],s[start]
            start+=1
            end-=1
        return "".join(s)