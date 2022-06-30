class Solution(object):
    def numberOfSteps(self, num):
        answer = 0
        while num > 0:
            if num % 2 == 0:
                num = num / 2
            else:
                num -= 1
            answer += 1
        return answer
            
        """
        :type num: int
        :rtype: int
        """
        