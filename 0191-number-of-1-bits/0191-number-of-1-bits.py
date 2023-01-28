from collections import Counter
class Solution:
    def hammingWeight(self, n: int) -> int:
        return Counter('{:032b}'.format(n))["1"]