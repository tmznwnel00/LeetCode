from collections import Counter
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner = Counter(map(lambda x:x[0], matches))
        loser = Counter(map(lambda x:x[1], matches))
        
        answer1 = list(filter(lambda key: key not in loser, winner))
        answer2 = list(filter(lambda item: loser[item] == 1, loser))
        
        return [sorted(answer1), sorted(answer2)]