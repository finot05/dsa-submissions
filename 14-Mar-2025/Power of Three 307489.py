# Problem: Power of Three - https://leetcode.com/problems/power-of-three/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def helper(n):
            if n == 1:
                return True
            elif n < 1:
                return False
            if n % 3 == 0:
                return helper(n//3)
            return False
        return helper(n)