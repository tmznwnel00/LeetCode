from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        answer = 0
        l = [[] for i in range(n)]
        d = defaultdict(int)
        d2 = defaultdict(list)
        for i in range(n):
            temp = set([])
            for j in range(i):
                if isConnected[i][j] == 1:
                    temp.add(j + 1)
                    temp.add(d[j + 1])
            if len(temp) == 0:
                val = i + 1
            else:
                val = min(temp)
            d[i + 1] = val
            d2[val].append(i + 1)
            # print(i + 1, temp)
            for t in temp:
                if d[t] != val:
                    # print(i + 1, t, d[t])
                    d2[val].extend(d2[d[t]])
                    for k in d2[d[t]]:
                        d[k] = val
                    
                    d2[val] = list(set(d2[val]))
                    
                    d[t] = val
        #     print(i + 1, d)
        #     print(i + 1, d2)
        # print(d)
        # print(d2)
        return len(set(d.values()))