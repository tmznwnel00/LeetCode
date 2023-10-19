class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []
        
        for i in s:
            if i != '#':
                s_stack.append(i)
            else:
                if s_stack == []:
                    continue
                s_stack.pop()
                
        for j in t:
            if j != '#':
                t_stack.append(j)
            else:
                if t_stack == []:
                    continue
                t_stack.pop()
                
        return s_stack == t_stack