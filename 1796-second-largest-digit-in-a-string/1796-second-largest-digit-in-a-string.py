class Solution:
    def secondHighest(self, s: str) -> int:
        s = list(s)
        digits = [item for item in s if item.isdigit()]
        uniqueDigits = set(digits)
        uniqueDigits = sorted(uniqueDigits)
        if len(uniqueDigits) > 1:
            return int(uniqueDigits[-2])
        return -1