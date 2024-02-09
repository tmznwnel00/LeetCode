from collections import defaultdict
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        answer = []
        nums.sort()
        dp = defaultdict(list)
        dp[1].append(nums[0])
        child = {}
        child[nums[0]] = nums[0]
        max_val = 1
        for i, num in enumerate(nums[1:]):
            temp = max_val
            while temp > 0:
                dp_list = dp[temp]
                for candidate in dp_list:
                    if num % candidate == 0:
                        dp[temp+1].append(num)
                        max_val = max(max_val, temp+1)
                        temp = 0
                        child[num] = candidate
                        break
                temp -= 1
            if num not in child:
                child[num] = num
                dp[1].append(num)
        
        pointer = dp[max_val][0]
        while True:
            answer.append(pointer)
            if pointer == child[pointer]:
                break
            pointer = child[pointer]
        return answer
            
        
                