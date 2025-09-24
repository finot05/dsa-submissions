# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        def dp(n):
            if n<2:
                return n
            if n==2:
                return 1
            if n not in memo:
                memo[n] = dp(n-1) + dp(n-2) + dp(n-3)
            return memo[n]
        return dp(n)