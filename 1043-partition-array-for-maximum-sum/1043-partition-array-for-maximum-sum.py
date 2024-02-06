class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [[0 for i in range(k)] for j in range(len(arr))]
        
        for j, num in enumerate(arr):
            for i in range(k):
                if j-i < 0:
                    break
                if i == 0:
                    dp[j][i] = max(dp[j-1]) + num
                else:
                    dp[j][i] = max(arr[j-i:j+1])*(i+1) + (max(dp[j-i-1]) if j-i-1 >= 0 else 0)
        return max(dp[-1])