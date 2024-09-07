class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counter = collections.Counter(deck)
        counts = list(counter.values())
        gcd = counts[0]
        for count in counts[1:]:
            gcd = math.gcd(gcd, count)
        return gcd > 1