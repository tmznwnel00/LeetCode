class Solution(object):
    def isValid(self, s):
        now = ''
        for i in range(len(s)):
            if s[i] == '(':
                now += '('
            elif s[i] == '[':
                now += '['
            elif s[i] == '{':
                now += '{'
            elif s[i] == ')':
                if len(now) == 0 or now[-1] != '(':
                    return False
                else:
                    now = now[:-1]
            elif s[i] == ']':
                if len(now) == 0 or now[-1] != '[':
                    return False
                else:
                    now = now[:-1]
            elif s[i] == '}':
                if len(now) == 0 or now[-1] != '{':
                    return False
                else:
                    now = now[:-1]
        if len(now) == 0:
            return True
        else:
            return False
    
        