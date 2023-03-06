class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [[0 ,0] for i in range(len(nums))]
        dp[0][0] = nums[0]
        
        for i in range(1, len(nums)):
            dp[i][1] = max(dp[i - 1][0], dp[i - 1][1])
            
            dp[i][0] = dp[i - 1][1] + nums[i]
        
        return max(dp[-1][0], dp[-1][1])
            