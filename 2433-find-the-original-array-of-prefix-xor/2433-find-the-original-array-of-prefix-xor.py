class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        answer = [pref[0]]
        
        for i in range(1, len(pref)):
            result = pref[i] ^ pref[i-1]
            answer.append(result)
            
        
        return answer