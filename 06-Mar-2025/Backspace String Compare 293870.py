# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stk = []
        t_stk = []
        for char in s:
            if char == '#':
                if s_stk:
                    s_stk.pop()
            else:
                s_stk.append(char)
        for char in t:
            if char == '#':
                if t_stk:
                    t_stk.pop()
            else:
                t_stk.append(char)
        return s_stk == t_stk