class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        answer = 0
        previous = 0
        current = 0
        for row in bank:
            for index in row:
                if index == '1':
                    current += 1
            if current == 0:
                continue
            else:
                answer += current * previous
                previous = current
                current = 0
                
        return answer
                
            
            