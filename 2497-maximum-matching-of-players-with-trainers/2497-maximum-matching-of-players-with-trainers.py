class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort(reverse = True)
        trainers.sort(reverse = True)
        i, j = 0, 0
        answer = 0
        while True:
            if players[i] <= trainers[j]:
                answer += 1
                i += 1
                j += 1
            else:
                i += 1
            
            if i == len(players) or j == len(trainers):
                break
        return answer
