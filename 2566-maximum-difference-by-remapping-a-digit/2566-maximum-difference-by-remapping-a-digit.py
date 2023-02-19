class Solution:
    def minMaxDifference(self, num: int) -> int:
        max_val = ''
        min_val = ''
        d1 = {}
        d2 = {}
        for i in str(num):
            if len(d1) == 0:
                if i == '9':
                    max_val += str(i)
                    continue
                else:
                    d1[i] = 9
                    max_val += '9'
            else:
                if i in d1:
                    max_val += '9'
                else:
                    max_val += str(i)
        for i in str(num):
            if len(d2) == 0:
                d2[i] = 0
            else:
                if i in d2 and len(min_val) != 0:
                    min_val += '0'
                elif i in d2:
                    continue
                else:
                    min_val += str(i)
        if min_val == '':
            min_val = '0'
        return int(max_val) - int(min_val)