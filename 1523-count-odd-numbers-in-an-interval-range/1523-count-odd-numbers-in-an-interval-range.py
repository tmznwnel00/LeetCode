class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low == high and low % 2 == 1:
            return 1
        elif low == high and low % 2 == 0:
            return 0
        elif low % 2 == 1 and high % 2 == 1:
            return (high - low) // 2 + 1
        elif low % 2 == 0 and high % 2 == 0:
            return (high - low) // 2
        else:
            return (high - low) // 2 + 1