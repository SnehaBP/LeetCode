class Solution:
    def judgeCircle(self, moves: str) -> bool:
        horigontal=0
        vertical=0
        for move in moves:
            if move=="R":
                horigontal+=1
            elif move=="L":
                horigontal-=1
            elif move=="U":
                vertical+=1
            elif move=="D":
                vertical-=1
        return horigontal==0 and vertical==0