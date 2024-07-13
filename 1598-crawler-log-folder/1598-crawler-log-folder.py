class Solution:
    def minOperations(self, logs: List[str]) -> int:
        step = 0
        
        for log in logs:
            if log.startswith('..'):
                if step == 0:
                    continue
                else:
                    step -= 1
            elif log.startswith('.'):
                continue
            else:
                step += 1
        return step