class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        string=['']*len(s)
        for i,index in enumerate(indices):
            string[index]=s[i]
        return ''.join(string)