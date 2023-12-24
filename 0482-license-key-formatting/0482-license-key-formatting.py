class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        string=s.replace("-","").upper()
        reversedString=string[::-1]
        formating="-".join(reversedString[i:i+k] for i in range(0,len(reversedString),k))
        formatedString=formating[::-1]
        return formatedString