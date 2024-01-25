class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        answer = 0
        dp = [[0 for i in range(len(text1))] for j in range(len(text2))]
        
        for i2, c2 in enumerate(text2):
            for i1, c1 in enumerate(text1):
                if c1 == c2:
                    if i1 > 0 and i2 > 0:
                        dp[i2][i1] = dp[max(0, i2-1)][max(0, i1-1)] + 1
                    else:
                        dp[i2][i1] = 1
                else:
                    dp[i2][i1] = max(dp[max(0, i2-1)][i1], dp[i2][max(0, i1-1)])

        return dp[-1][-1]
                
                
                