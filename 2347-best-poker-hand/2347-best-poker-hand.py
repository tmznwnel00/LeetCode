class Solution(object):
    def bestHand(self, ranks, suits):
        a = suits.count('a')
        b = suits.count('b')
        c = suits.count('c')
        d = suits.count('d')
        if a == 5 or b == 5 or c == 5 or d == 5:
            return "Flush"
        else:
            for i in range(3):
                if ranks.count(ranks[i]) >= 3:
                    return "Three of a Kind"
            for i in range(4):
                if ranks.count(ranks[i]) >= 2:
                    return "Pair"
            return "High Card"
        