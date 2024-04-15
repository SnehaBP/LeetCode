class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bullCount=0
        cowsCount=0
        secret=list(secret)
        guess=list(guess)
        for i in range(len(guess)):
            if secret[i]==guess[i]:
                bullCount+=1
                secret[i]=guess[i]= None
        for dig in guess:
            if  dig is not None and dig in secret:
                cowsCount+=1
                secret[secret.index(dig)]= None
        return "".join(str(bullCount)+"A"+str(cowsCount)+"B")