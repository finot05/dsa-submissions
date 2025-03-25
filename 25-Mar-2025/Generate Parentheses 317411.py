# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        stk, arr = [], []
        
        def combination(i):
            if i == n*2:
                if not stk:
                    ans.append(''.join(arr))
                return

            stk.append('(')
            arr.append('(')
            combination(i+1)
            stk.pop()
            arr.pop()

            if stk:
                stk.pop()
                arr.append(')')
                combination(i+1)
                stk.append('(')
                arr.pop()
        
        combination(0)

        return ans