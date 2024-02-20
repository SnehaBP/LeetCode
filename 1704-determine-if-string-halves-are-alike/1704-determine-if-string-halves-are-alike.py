class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        halfLength=len(s)//2
        a=s[0:halfLength]
        b=s[halfLength:len(s)]
        countOfVowelIna=0
        countOfVowelInb=0
        for char in a:
            if char=='a'or char=='e'or char=='i'or char=='o'or char=='u'or char=='A'or char=='E'or char=='I'or char=='O'or char=='U':
                countOfVowelIna+=1
        for char in b:
            if char=='a'or char=='e'or char=='i'or char=='o'or char=='u'or char=='A'or char=='E'or char=='I'or char=='O'or char=='U':
                countOfVowelInb+=1
        return countOfVowelIna==countOfVowelInb