class Solution(object):
    def romanToInt(self, s):
        answer = 0
        length = len(s)
        l = []
        d = {}
        d = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000, "IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
        for i in range(length):
            if i in l:
                continue
            if s[i:i+2] in d:
                l.append(i+1)
                answer += d[s[i:i+2]]
            else:
                answer += d[s[i]]
        return answer