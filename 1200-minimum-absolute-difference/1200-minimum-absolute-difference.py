class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        min_val = min(min(arr), 0)
        max_val = max(arr)
        l = [0 for i in range(max_val - min_val + 1)]
        
        for a in arr:
            l[a - min_val] += 1
        answer = []
        left = -1
        check = max_val - min_val + 1
        
        for index, value in enumerate(l):
            if value == 1:
                if left == -1:
                    left = index
                else:
                    if index - left < check:
                        answer = [[left + min_val, index + min_val]]
                        check = index - left
                        
                    elif index - left == check:
                        answer.append([left + min_val, index + min_val])

                    left = index
        return answer