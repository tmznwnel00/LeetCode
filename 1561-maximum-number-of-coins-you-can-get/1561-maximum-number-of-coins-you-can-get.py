class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        answer = 0
        for i in range(len(piles)//3):
            piles.pop(0)
            answer += piles.pop(0)
            piles.pop()
        return answer