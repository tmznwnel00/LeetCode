class Solution(object):
    def maximumWealth(self, accounts):
        answer = 0
        for i in range(len(accounts)):
            if sum(accounts[i]) > answer:
                answer = sum(accounts[i])
        return answer
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        