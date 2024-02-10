from collections import defaultdict
class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def checkPalindrome(st):
            for pointer in range(len(st)//2):
                if st[pointer] != st[-pointer-1]:
                    return False
            return True
                
        answer = 0
        char_dict = defaultdict(list)
        for i, c in enumerate(s):
            char_dict[c].append(i)
            for ch in char_dict[c]:
                if checkPalindrome(s[ch:i+1]):
                    answer += 1
        return answer
                
            
            
            
            