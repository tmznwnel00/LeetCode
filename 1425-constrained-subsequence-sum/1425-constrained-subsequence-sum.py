import heapq
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = [0 for i in range(len(nums))]
        
        dp[-1] = nums[-1]
        heap = []
        heapify(heap)
        heappush(heap, (-nums[-1], len(nums)-1))
        for i in range(len(nums)-2, -1, -1):
            while heap[0][1] - i > k:
                heappop(heap)
            dp[i] = max(0, -1*heap[0][0]) + nums[i]
            heappush(heap, (-dp[i], i))
        return max(dp)
