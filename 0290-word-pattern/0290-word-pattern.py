class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        
        pattern_to_char = {}
        word_to_char = {}
        
        for char, word in zip(pattern, words):
            if char in pattern_to_char:
                if pattern_to_char[char] != word:
                    return False
            else:
                pattern_to_char[char] = word
                
            if word in word_to_char:
                if word_to_char[word] != char:
                    return False
            else:
                word_to_char[word] = char
                
        return True