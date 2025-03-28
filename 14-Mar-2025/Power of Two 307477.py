# Problem: Power of Two - https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def helper(n):
            if n == 1:
                return True
            elif n < 1:
                return False
            return helper(n / 2)
        return helper(n)