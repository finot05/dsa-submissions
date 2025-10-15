# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(t, i):
            if i == len(nums):
                return 1 if t == 0 else 0

            if (t, i) in memo:
                return memo[(t, i)]

            memo[(t,i)] = dp(t-nums[i], i+1) + dp(t+nums[i], i+1)
            return memo[(t, i)]
            
        return dp(target, 0)