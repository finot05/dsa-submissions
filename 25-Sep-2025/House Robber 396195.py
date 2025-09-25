# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def dp(i):
            if i >= len(nums):
                return 0

            if i not in memo:
                rob = nums[i] + dp(i + 2)
                skip = dp(i + 1)
                memo[i] = max(rob, skip)
            
            return memo[i]

        return dp(0)