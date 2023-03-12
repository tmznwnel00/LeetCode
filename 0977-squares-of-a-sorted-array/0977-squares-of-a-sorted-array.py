class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        def pow_tow(l):
            return pow(l, 2)
        
        return sorted(list(map(pow_tow, nums)))