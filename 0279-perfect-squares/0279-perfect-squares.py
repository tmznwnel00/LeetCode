class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        dp[1] = 1
        for i in range(2, n+1):
            sqrt = int(math.sqrt(i))
            min_val = i
            if i == sqrt**2:
                dp[i] = 1
                continue
            for j in range(1, sqrt+1):
                min_val = min(min_val, 1+dp[i-j**2])
            dp[i] = min_val
        return dp[n]
            
            