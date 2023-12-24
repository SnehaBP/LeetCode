class Solution:
    def findComplement(self, num: int) -> int:
        bitmask = (1 << num.bit_length()) - 1
        complement = num ^ bitmask
        return complement
