# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution:
    # def (n):
    #     if n % 4 != 0:
    #         return n % 4
    #     num_of_visibility(n//2)
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        if n%4 != 0:
            return False
        return self.isPowerOfFour(n//4)
        # if n<=0:
        #     return False
        # while n%4 == 0:
        #     n //= 4
            
        # return n == 1