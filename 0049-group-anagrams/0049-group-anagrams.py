class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict={}
        for word in strs:
            sortedWord=''.join(sorted(word))
            if sortedWord not in anagramDict:
                anagramDict[sortedWord]=[]
            anagramDict[sortedWord].append(word)
        return anagramDict.values()