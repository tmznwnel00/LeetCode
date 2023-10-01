class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        answer = ''
        for c in s:
            if c == ' ':
                answer += ''.join(reversed(stack))
                answer += ' '
                stack = []
            else:
                stack.append(c)
        answer += ''.join(reversed(stack))
        return answer