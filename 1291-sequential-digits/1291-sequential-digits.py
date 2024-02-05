class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        low_length = len(str(low))
        high_length = len(str(high))
        answer = []
        start = []
        for i in range(1, 10-low_length+1):
            temp = ''
            for k in range(low_length):
                temp += str(i+k)
            start.append(temp)
        
        while start:
            now = start.pop(0)
            if int(now) >= low and int(now) <= high:
                answer.append(int(now))
            if now[-1] != '9' and len(now) < high_length:
                now += str(int(now[-1])+1)
                start.append(now)

        return answer
            