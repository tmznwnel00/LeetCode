import heapq
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        heapify(arr)
        answer = 0
        for i in range(len(arr)):
            while True and arr:
                now = heappop(arr)
                if now < i + 1:
                    continue
                else:
                    answer += 1
                    break
        return answer
            