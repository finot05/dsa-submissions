# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot % 2:
            return False
        targ = tot // 2
        memo = {}

        def dp(i, cur):
            if cur == 0:
                return True
            if i == len(nums) or cur < 0:
                return False
            if (i, cur) in memo:
                return memo[(i, cur)]

            memo[(i, cur)] = dp(i+1, cur-nums[i]) or dp(i+1, cur)
            return memo[(i, cur)]

        return dp(0, targ)
