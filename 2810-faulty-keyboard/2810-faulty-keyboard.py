class Solution:
    def finalString(self, s: str) -> str:
        result = ""
        for char in s:
            if char != 'i':
                result += char
            else:
                result = result[::-1]
        return result