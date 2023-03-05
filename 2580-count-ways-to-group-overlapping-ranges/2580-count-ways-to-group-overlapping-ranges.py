class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges = sorted(ranges)
        l = ranges[0]
        length = 1
        for index in range(len(ranges)):
            i = ranges[index][0]
            j = ranges[index][1]
            if index == 0:
                continue
            
            if i > l[1]:
                length += 1
                l = [i, j]
                continue
            else:
                l = [l[0], max(j, l[1])]
                
        return (2 ** length) % (10**9 + 7)