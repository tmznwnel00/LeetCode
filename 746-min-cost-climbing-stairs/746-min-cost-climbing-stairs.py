class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.append(0)
        answer = 0
        l = []
        l.append(cost[0])
        l.append(cost[1])
        for i in range(2, len(cost)):
            l.append(min(l[i - 2] + cost[i], l[i - 1] + cost[i]))
        return l[-1]
            
            
        