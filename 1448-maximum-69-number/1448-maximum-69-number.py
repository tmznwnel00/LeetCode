class Solution:
    def maximum69Number (self, num: int) -> int:
        answer = ""
        flag_i = -1

        for i, c in enumerate(str(num)):
            if c == "6":
                answer += "9"
                flag_i = i
                break
            answer += c
        
        if flag_i != -1:
            answer += str(num)[flag_i + 1:]
        return int(answer)