class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        gain.insert(0, 0)
        print(gain)
        for index, g in enumerate(gain[1:]):
            gain[index+1] += gain[index]
        
        return max(gain)