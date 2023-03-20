class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = ''
        max_val = 0
        for i in s:
            if i not in answer:
                answer += i
            else:
                max_val = max(max_val, len(answer))
                answer = answer[answer.find(i) + 1:]
                answer += i
        
        
        return max(max_val, len(answer))