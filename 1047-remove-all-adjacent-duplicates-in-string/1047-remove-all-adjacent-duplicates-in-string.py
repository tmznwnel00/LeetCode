class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = ''
        for i in range(len(s)):
            if len(l) == 0:
                l += s[i]
            elif l[-1] == s[i]:
                l = l[:-1]
            else:
                l += s[i]
        return l