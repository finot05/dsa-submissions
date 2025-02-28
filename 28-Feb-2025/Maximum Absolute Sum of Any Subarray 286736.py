# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        cur_max = tot_max = nums[0]
        cur_min = tot_min = nums[0]
        for i in range(1, len(nums)):
            cur_max = max(cur_max + nums[i], nums[i])
            cur_min = min(cur_min + nums[i], nums[i])
            if cur_max > tot_max:
                tot_max = cur_max
            if cur_min < tot_min:
                tot_min = cur_min
        return max(abs(tot_min), abs(tot_max))