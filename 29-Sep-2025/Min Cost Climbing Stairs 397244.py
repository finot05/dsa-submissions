# Problem: Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dp(i):
            if i >= len(cost):
                return 0
            
            if i not in memo:
                memo[i] = min(cost[i] + dp(i+1), cost[i] + dp(i+2))
            return memo[i]
        return min(dp(0), dp(1))