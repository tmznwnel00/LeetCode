class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        l = [[] for i in range(numRows)]
        now = 0
        plus = 0
        for i in s:
            l[now].append(i)
            if now == 0:
                plus = 0
            elif now == numRows -1 :
                plus = 1
            if plus == 0:
                now += 1
            else:
                now -= 1
        answer = ''
        for q in l:
            j = ''.join(q)
            answer += j
        return answer
        