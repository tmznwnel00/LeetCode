class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        start = 1
        index = 0
        cnt = 0
        while True:
            if index >= len(arr):
                cnt += 1
            elif start < arr[index]:
                cnt += 1
            else:
                index += 1
            
            if cnt == k:
                return start
            start += 1