from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        if Counter(s) == Counter(t):
            return True
        else:
            return False
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        