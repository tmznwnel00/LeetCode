class Solution(object):
    def wiggleMaxLength(self, nums):
        l = []
        plus = 0
        answer = 0
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 0:
                continue
            elif nums[i + 1] - nums[i] > 0:
                if answer == 0:
                    answer += 1
                    plus = 1
                else:
                    if plus == 1:
                        continue
                    else:
                        plus = 1
                        answer += 1
            else:
                if answer == 0:
                    answer += 1
                    plus = -1
                else:
                    if plus == -1:
                        continue
                    else:
                        plus = -1
                        answer += 1
                        
                        
        return answer+1
                
        """
        :type nums: List[int]
        :rtype: int
        """
        