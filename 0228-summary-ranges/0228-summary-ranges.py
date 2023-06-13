class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums == []:
            return nums
        min_val = min(nums) - 1
        start, end = min_val, min_val
        answer = []
        
        for num in nums:
            if start == min_val:
                start = num
            elif num == end + 1 or num == start + 1:
                end = num
            else:
                if end == min_val:
                    answer.append(f'{start}')
                else:
                    answer.append(f'{start}->{end}')
                    end = min_val
                start = num
        if end == min_val:
            
            answer.append(f'{start}')    
        else:
            answer.append(f'{start}->{end}')
           
        return answer
            
            