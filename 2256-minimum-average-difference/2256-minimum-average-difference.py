class Solution(object):
    def minimumAverageDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        d = []
        if l == 1:
            return 0
        a1 = 0
        a2 = sum(nums)
        for i in range(1, l + 1):
            a1 += nums[i-1]
            a2 -= nums[i-1]
            if i == l:
                d.append(a1 // i)
            else:
                d.append(abs((a1 // i) - a2 // (l-i)))
        return d.index(min(d))