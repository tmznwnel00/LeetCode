from collections import defaultdict
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        sorted_index = [i[0] for i in sorted(enumerate(endTime), key=lambda x:x[1])]
        sorted_end = sorted(endTime)
        end = max(endTime) + 1
        dp = defaultdict(int)
        answer = 0
        for index in sorted_index:
            
            j = endTime[index] 
            temp = dp[j]
            
            start = startTime[index]
            index2 = bisect_right(sorted_end, start) - 1
            if index2 == -1:
                prev_val = 0
            else:
                prev_val = dp[sorted_end[index2]]
            dp[j] = max(temp, prev_val + profit[index], answer)
            if dp[j] > answer:
                answer = dp[j]

        return answer
            
            
            
            