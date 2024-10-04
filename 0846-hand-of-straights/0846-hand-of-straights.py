from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        c = Counter(hand)

        for i in range(len(hand)//groupSize):
            m = min(c)
            c[m] -= 1
            if c[m] == 0:
                del c[m]
            for j in range(1, groupSize):
                if m+j in c:
                    c[m+j] -= 1
                    if c[m+j] == 0:
                        del c[m+j]
                else:
                    return False
                
        return True