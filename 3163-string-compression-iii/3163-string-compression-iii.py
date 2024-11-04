class Solution:
    def compressedString(self, word: str) -> str:
        answer = ""
        cnt = 0
        now = word[0]
        for c in word:
            if c != now or cnt == 9:
                answer += str(cnt)
                answer += now
                now = c
                cnt = 1
            else:
                cnt += 1
        
        answer += str(cnt)
        answer += now
        return answer
            
                