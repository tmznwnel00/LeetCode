class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        stack2 = []
        answer = ""
        for i, c in enumerate(s):
            if c == ')' and stack == []:
                stack2.append(i)
            elif c == ')' and stack:
                stack.pop()
            elif c == '(':
                stack.append(i)
            answer +=c 
        stack = stack + stack2
        for i in sorted(stack, reverse = True):
            answer = answer[:i] + answer[i+1:]
        return answer
            
        
                
        