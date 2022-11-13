class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = s.split(' ')
        t = ""
        for i in range(len(d)):
            if d[-i - 1] == u'':
                continue
            else:
                t += d[-i -1]
                t += ' '
        if len(t) < 2:
            return t
        else:
            return t[:-1]
        