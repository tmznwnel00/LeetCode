from collections import Counter
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        c = Counter(nums)
        visited = set([])
        answer = 0
        for num in sorted(c.keys()):
            if num in visited:
                continue
            if num == 1:
                if c[num] % 2 == 1:
                    temp = c[num]
                else:
                    temp = c[num] - 1
            else:
                now = num
                if c[now] >= 2:
                    temp = 0
                    while now ** 2 in c:
                        if c[now ** 2] >= 2:
                            now = now ** 2
                            temp += 2
                            visited.add(now)
                        else:
                            temp += 1
                            break
                    if temp % 2 == 0:
                        temp += 1
                    else:
                        temp += 2
                else:
                    temp = 1
            if temp > answer:
                answer = temp
        return answer
                
                
                