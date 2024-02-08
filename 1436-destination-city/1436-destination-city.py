class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outgoing = defaultdict(int)
        incoming = defaultdict(int)

        for path in paths:
            outgoing[path[0]] += 1
            incoming[path[1]] += 1

        for city in incoming:
            if outgoing[city] == 0:
                return city