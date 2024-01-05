class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        words = sentence.split()

        res = [(word + "ma" if word[0].lower() in vowels else word[1:] + word[0] + "ma") +'a' * (index + 1) for index, word in enumerate(words)]

        return ' '.join(res)