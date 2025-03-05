# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stk = []
        for elem in path:
            if elem == '..':
                if stk:
                    stk.pop()
            elif elem != '.' and elem != '':
                stk.append(elem)
        return '/'+'/'.join(stk)