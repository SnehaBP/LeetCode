class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        letters = list(string.ascii_lowercase)
        my_dict = {letters[i] : widths[i] for i in range(len(letters))}
        lineCount = 1
        current_width = 0
        for l in s:
            width = my_dict[l] 
            if current_width + width > 100:
                lineCount += 1  
                current_width = width  
            else:
                current_width += width
        return [lineCount, current_width]