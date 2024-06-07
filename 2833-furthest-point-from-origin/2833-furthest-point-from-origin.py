class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        count = 0
        for move in moves:
            if move == 'L':
                count -= 1
            elif move == 'R':
                count += 1
        wildCardCount = moves.count('_')
        return abs(count) + wildCardCount