# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        maximum = float('-inf')
        for i in range(len(nums)):
            current_sum += nums[i]
            maximum = max(maximum, current_sum)
            if current_sum < 0 :
                current_sum = 0
        return maximum