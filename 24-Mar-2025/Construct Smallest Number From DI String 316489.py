# Problem: Construct Smallest Number From DI String - https://leetcode.com/problems/construct-smallest-number-from-di-string/description/

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stk, res = [], []
        num = 1
        for char in pattern:
            stk.append(num)
            num += 1
            if char == 'I':
                while stk:
                    res.append(str(stk.pop()))

        stk.append(num)
        while stk:
            res.append(str(stk.pop()))

        return ''.join(res)