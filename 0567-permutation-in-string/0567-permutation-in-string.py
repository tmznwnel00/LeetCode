from itertools import permutations
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        for i in range(len(s2) - length + 1):
            if Counter(s2[i : i + length]) == Counter(s1):
                return True
        return False