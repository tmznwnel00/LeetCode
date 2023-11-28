from math import prod
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        cnt = 0
        now = 1
        answer = []
        for c in corridor:
            if c == 'S':
                if cnt == 2:
                    cnt = 1
                    answer.append(now)
                    now = 1
                else:
                    cnt += 1
            else:
                if cnt == 2:
                    now += 1
                else:
                    continue
        if cnt == 1:
            return 0
        if answer == [] and cnt == 2:
            return 1
        elif answer == []:
            return 0
        return prod(answer) % (10**9+7)