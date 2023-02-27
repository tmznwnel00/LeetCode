class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        buy = prices[0]
        for i in prices:
            if i < buy:
                buy = i
            answer = max(answer, i - buy)
        return max(0, answer)