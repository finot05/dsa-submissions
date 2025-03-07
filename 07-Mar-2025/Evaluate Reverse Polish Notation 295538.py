# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for i in range(len(tokens)):
            if tokens[i] in '+-/*':
                b = stk.pop()
                a = stk.pop()
                if tokens[i] == '+':
                    stk.append(a + b)
                elif tokens[i] == '-':
                    stk.append(a - b) 
                elif tokens[i] == '*':
                    stk.append(a * b) 
                else:
                    stk.append(int(a / b))
            else:
                stk.append(int(tokens[i]))
        return stk[0]