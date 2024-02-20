class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudesList=[0]
        for i in range(len(gain)):
            altitudesList.append(altitudesList[-1]+gain[i])
        return max(altitudesList)