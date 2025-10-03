# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        def dp(i, j):
            if i == len(triangle)-1:
                return triangle[i][j]
            if (i, j) not in memo:
                l = dp(i+1, j)
                r = dp(i+1, j+1)
                memo[(i, j)] =  triangle[i][j] + min(l, r)
            return memo[(i, j)]
        return dp(0, 0)