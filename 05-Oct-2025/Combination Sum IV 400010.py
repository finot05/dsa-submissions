# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(target):
            if target==0:
                return 1
            if target < 0:
                return 0
            
            if target in memo:
                return memo[target]
            tot = 0
            for i in range(len(nums)):
                tot += dp(target-nums[i])
                
            memo[target] = tot
            return tot

        return dp(target)